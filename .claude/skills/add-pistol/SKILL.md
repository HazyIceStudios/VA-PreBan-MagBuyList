---
name: add-pistol
description: Adds a new pistol entry to the VA Pre-Ban Mag Buy List HTML report, then commits and deploys to GitHub Pages. Use this whenever the user wants to add a gun, pistol, or firearm to the list — phrases like "add [gun] to the list", "include [model] in the report", "add [pistol]", or just a gun name typed alone. Always use this skill rather than manually editing the HTML.
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
| **Notes** | Critical warnings or standout facts (frame damage risk, proprietary-only mags, compatibility caveats). Empty string if nothing notable. |

---

## Step 2 — Determine rank

Read `output/mag-buy-list.html` and find the highest `rank:` value in the DATA array. Assign the new entry `rank + 1`. New entries are always `src: "rec"`.

---

## Step 3 — Build all entry fields

Every field below is required. Do not omit any.

```
rank       — next integer after current highest
rd         — string of rank (e.g., "35")
src        — "rec"
model      — full name with variants; add caliber in parens only if not obvious
             e.g., "HK USP Compact", "Ruger PC Carbine (9mm)"
cal        — caliber: "9mm" | "10mm" | ".22" | ".380" | ".45" | other
buyPistols — array of individual variant search strings for GunBroker
             each entry is a distinct purchasable model
             e.g., ["HK USP 9mm", "HK USP Compact 9mm", "HK USP 45"]
buyMags    — array of mag search strings for Google Shopping
             one entry per distinct capacity option
             format: "[Brand] [Model] [caliber] [N]rd"
             e.g., ["HK USP 9mm 15rd", "HK USP 9mm 18rd extended"]
purpose    — "Primary / Secondary" slash-separated string
priceMin   — integer MSRP low
priceMax   — integer MSRP high
mags       — human-readable array matching the mag options you researched
             e.g., ["15rd (OEM standard)", "18rd (extended)"]
preBan     — boolean
rec        — recommendation string (what to buy, why, any critical notes)
magPrice   — cost estimate string
brands     — OEM + aftermarket brands as a single string
compat     — compatible pistols and PCCs as a single string; note any cross-compat
             restrictions explicitly
note       — warning/quirk string, or "" if none
linkMag    — "" (links are generated dynamically from buyMags — leave empty)
```

---

## Step 4 — Insert into the HTML

Open `output/mag-buy-list.html`. Find the end of the DATA array — it's the line that reads `];` after the last entry's closing `}`. Insert the new entry **before** that line, separated by a comma from the previous entry. Match the formatting style of existing entries exactly (two-space indent, one field per line).

---

## Step 5 — Commit and push to master

```bash
cd "C:\Users\micwe\OneDrive\ClaudeRepo\Guns\HighCapacityMagBuyList"
git add output/mag-buy-list.html
git commit -m "Add [MODEL] to mag buy list"
git push origin master
```

---

## Step 6 — Deploy to GitHub Pages

The `gh-pages` branch contains only `index.html` (a copy of the report). Update it:

```powershell
# Windows — copy updated HTML before switching branches
Copy-Item "output\mag-buy-list.html" "$env:TEMP\pages-update.html"
git checkout gh-pages
Copy-Item "$env:TEMP\pages-update.html" "index.html"
git add index.html
git commit -m "Deploy to Pages — add [MODEL]"
git push origin gh-pages
git checkout master
```

---

## Step 7 — Confirm

Tell the user:
- The pistol that was added and its rank
- Whether pre-ban action is needed (and what to buy if so)
- The live Pages URL: https://hazyicestudios.github.io/VA-PreBan-MagBuyList/
