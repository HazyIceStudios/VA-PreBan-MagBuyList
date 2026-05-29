---
name: add-pistol
description: Adds a new pistol entry to the VA Pre-Ban Mag Buy List — inserts into the SQLite database, regenerates the HTML report, then commits and deploys to GitHub Pages. Use this whenever the user wants to add a gun, pistol, or firearm to the list — phrases like "add [gun] to the list", "include [model] in the report", "add [pistol]", or just a gun name typed alone. Always use this skill rather than manually editing the HTML or database.
disable-model-invocation: true
---

Add a new pistol entry to the VA Pre-Ban mag buy list.

## Input

`$ARGUMENTS` — the pistol name/model to add (e.g., "HK USP 9mm", "Ruger PC Carbine")

## Project path

`C:\Users\micwe\OneDrive\ClaudeRepo\Guns\HighCapacityMagBuyList`

---

## Step 1 — Research the pistol

Use your training knowledge to determine all of the following. Be specific and accurate — this is a purchasing guide and the user will act on it.

| Field | What to find |
|-------|-------------|
| **Caliber(s)** | Primary caliber (9mm, 10mm, .45 ACP, .22 LR, .380 ACP, etc.) |
| **Purpose** | 2–3 slash-separated tags (e.g., "Home Defense / Duty / Competition") |
| **Price range** | MSRP low and high in USD (integers) |
| **Magazine options** | All factory and popular aftermarket capacities — include brand/variant context in parens (e.g., "17rd (OEM)", "19rd (Mec-Gar)", "10rd (flush)") |
| **Pre-ban flag** | `true` if ANY mag option exceeds 15 rounds; `false` if all options ≤ 15rd |
| **Recommendation** | What to buy before the ban and why — 1–2 sentences, specific |
| **Est. mag price** | Per-mag cost range for the recommended mags (e.g., "~$35–45/mag OEM (17rd)") |
| **Mag brands** | OEM first, then popular aftermarket (e.g., "Glock (OEM), Magpul PMAG, ETS") |
| **Compatible guns / PCCs** | Other pistols and carbines sharing the same magazine — be thorough |
| **Notes** | Critical warnings or standout facts. Empty string if nothing notable. |

---

## Step 2 — Determine rank

Query the database for the current highest rank:

```bash
python -c "import sqlite3; c=sqlite3.connect('data/pistols.db'); print(c.execute('SELECT MAX(rank) FROM pistols').fetchone()[0])"
```

New entry rank = that value + 1. New entries are always `src="rec"`.

---

## Step 3 — Field reference

Every field below is required:

```
rank       — next integer (from Step 2)
rd         — string of rank (e.g., "36")
src        — "rec"
model      — full name; add caliber in parens if not obvious
cal        — "9mm" | "10mm" | ".22" | ".380" | ".45" | other
purpose    — "Primary / Secondary" slash-separated string
price_min  — integer MSRP low
price_max  — integer MSRP high
pre_ban    — True or False
rec        — recommendation string
mag_price  — cost estimate string (e.g., "~$35–45/mag OEM (17rd)")
brands     — OEM + aftermarket brands as a single string
compat     — compatible pistols and PCCs as a single string
note       — warning/quirk string, or "" if none
link_mag   — "" (leave empty — links generated from buy_mags)
buy_pistols— list of individual variant search strings for GunBroker
buy_mags   — list of mag search strings for Google (one per capacity)
             format: "[Brand] [Model] [caliber] [N]rd"
mags       — human-readable list of mag options
             e.g., ["17rd (OEM)", "20rd (extended)"]
```

---

## Step 4 — Insert into the database

Append a new dict to the `PISTOLS` list in `scripts/init_db.py`, then rebuild:

```bash
cd "C:\Users\micwe\OneDrive\ClaudeRepo\Guns\HighCapacityMagBuyList"
python scripts/init_db.py
python scripts/generate_report.py
```

This recreates the database from the full PISTOLS list and regenerates `output/mag-buy-list.html`.

---

## Step 5 — Commit and push to master

```bash
git add data/pistols.db scripts/init_db.py output/mag-buy-list.html
git commit -m "Add [MODEL] to mag buy list"
git push origin master
```

---

## Step 6 — Deploy to GitHub Pages

```powershell
Copy-Item "output\mag-buy-list.html" "$env:TEMP\pages-update.html"
git checkout gh-pages
Copy-Item "$env:TEMP\pages-update.html" "index.html" -Force
git add index.html
git commit -m "Deploy to Pages — add [MODEL]"
git push origin gh-pages
git checkout master
```

---

## Step 7 — Confirm

Tell the user:
- The pistol added and its rank
- Whether pre-ban action is needed (and what to buy if so)
- Live URL: https://hazyicestudios.github.io/VA-PreBan-MagBuyList/
