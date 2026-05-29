"""
Reads data/pistols.db and regenerates output/mag-buy-list.html.
Run from the project root: python scripts/generate_report.py
"""
import sqlite3, json, re, pathlib

ROOT     = pathlib.Path(__file__).parent.parent
DB       = ROOT / "data" / "pistols.db"
TEMPLATE = ROOT / "scripts" / "template.html"
OUTPUT   = ROOT / "output" / "mag-buy-list.html"


def load_data():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row

    pistols = con.execute("SELECT * FROM pistols ORDER BY rank").fetchall()
    result = []

    for p in pistols:
        pid = p["id"]

        buy_pistols = [r["search_term"] for r in
                       con.execute("SELECT search_term FROM buy_pistols WHERE pistol_id=? ORDER BY sort_order", (pid,))]
        mags = [r["display"] for r in
                con.execute("SELECT display FROM mag_options WHERE pistol_id=? ORDER BY sort_order", (pid,))]
        buy_mags = [r["search_term"] for r in
                    con.execute("SELECT search_term FROM buy_mags WHERE pistol_id=? ORDER BY sort_order", (pid,))]

        result.append({
            "rank":        p["rank"],
            "rd":          p["rd"],
            "src":         p["src"],
            "model":       p["model"],
            "cal":         p["cal"],
            "buyPistols":  buy_pistols,
            "buyMags":     buy_mags,
            "purpose":     p["purpose"],
            "priceMin":    p["price_min"],
            "priceMax":    p["price_max"],
            "mags":        mags,
            "preBan":      bool(p["pre_ban"]),
            "rec":         p["rec"],
            "magPrice":    p["mag_price"],
            "brands":      p["brands"],
            "compat":      p["compat"],
            "note":        p["note"],
            "linkMag":     p["link_mag"],
        })

    con.close()
    return result


def generate():
    if not DB.exists():
        raise FileNotFoundError(f"Database not found: {DB}\nRun: python scripts/init_db.py")

    data = load_data()
    js   = json.dumps(data, indent=2, ensure_ascii=False)

    template = TEMPLATE.read_text(encoding="utf-8")
    output   = template.replace("/*__DATA__*/", js, 1)

    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(output, encoding="utf-8")
    print(f"Generated {OUTPUT} ({len(data)} pistols)")


if __name__ == "__main__":
    generate()
