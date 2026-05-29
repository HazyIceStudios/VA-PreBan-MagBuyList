CREATE TABLE IF NOT EXISTS pistols (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    rank      REAL    NOT NULL,
    rd        TEXT    NOT NULL,
    src       TEXT    NOT NULL CHECK(src IN ('list','rec')),
    model     TEXT    NOT NULL,
    cal       TEXT    NOT NULL,
    purpose   TEXT    NOT NULL,
    price_min INTEGER NOT NULL,
    price_max INTEGER NOT NULL,
    pre_ban   INTEGER NOT NULL CHECK(pre_ban IN (0,1)),
    rec       TEXT    NOT NULL DEFAULT '',
    mag_price TEXT    NOT NULL DEFAULT '',
    brands    TEXT    NOT NULL DEFAULT '',
    compat    TEXT    NOT NULL DEFAULT '',
    note      TEXT    NOT NULL DEFAULT '',
    link_mag  TEXT    NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS buy_pistols (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    pistol_id   INTEGER NOT NULL REFERENCES pistols(id) ON DELETE CASCADE,
    search_term TEXT    NOT NULL,
    sort_order  INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS mag_options (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    pistol_id INTEGER NOT NULL REFERENCES pistols(id) ON DELETE CASCADE,
    display   TEXT    NOT NULL,
    sort_order INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS buy_mags (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    pistol_id   INTEGER NOT NULL REFERENCES pistols(id) ON DELETE CASCADE,
    search_term TEXT    NOT NULL,
    sort_order  INTEGER NOT NULL DEFAULT 0
);
