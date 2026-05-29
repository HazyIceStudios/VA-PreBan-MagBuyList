---
name: generate-report
description: Regenerates the mag-buy-list HTML report from the SQLite database, then commits and deploys to GitHub Pages. Use this whenever the user says "publish", "deploy", "push to pages", "update the site", "generate the report", "sync", "regenerate", "rebuild", or "refresh". Also use when the database has been edited and the HTML needs to be brought up to date.
disable-model-invocation: true
---

Regenerate `output/mag-buy-list.html` from the database and deploy to GitHub Pages.

## Project path

`C:\Users\micwe\OneDrive\ClaudeRepo\Guns\HighCapacityMagBuyList`

---

## Step 1 — Regenerate the HTML from the database

```bash
cd "C:\Users\micwe\OneDrive\ClaudeRepo\Guns\HighCapacityMagBuyList"
python scripts/generate_report.py
```

This reads `data/pistols.db` and writes a fresh `output/mag-buy-list.html`.

---

## Step 2 — Check for changes and commit to master

```bash
git status
```

If `output/mag-buy-list.html` (or `data/pistols.db`) has changes, commit them:

```bash
git add output/mag-buy-list.html data/pistols.db
git commit -m "Regenerate report from database"
git push origin master
```

If already clean and up to date, skip to Step 3.

---

## Step 3 — Deploy to GitHub Pages

```powershell
Copy-Item "output\mag-buy-list.html" "$env:TEMP\pages-update.html"
git checkout gh-pages
Copy-Item "$env:TEMP\pages-update.html" "index.html" -Force
git add index.html
git commit -m "Deploy to Pages"
git push origin gh-pages
git checkout master
```

If `index.html` has no changes (already in sync), the commit will be skipped automatically.

---

## Step 4 — Confirm

Tell the user the report is live at:
**https://hazyicestudios.github.io/VA-PreBan-MagBuyList/**

Note: GitHub Pages can take 1–2 minutes to reflect the update after pushing.
