---
name: generate-report
description: Commits the current mag-buy-list HTML report and deploys it to GitHub Pages. Use this whenever the user says "publish", "deploy", "push to pages", "update the site", "generate the report", "sync", or has just finished making edits and wants them live. Also triggers when the user asks to "regenerate", "rebuild", or "refresh" the report without specifying a data change.
disable-model-invocation: true
---

Commit the current state of `output/mag-buy-list.html` and deploy it to GitHub Pages.

## Project path

`C:\Users\micwe\OneDrive\ClaudeRepo\Guns\HighCapacityMagBuyList`

---

## Step 1 — Check for uncommitted changes

```bash
cd "C:\Users\micwe\OneDrive\ClaudeRepo\Guns\HighCapacityMagBuyList"
git status
```

If `output/mag-buy-list.html` has no changes (already committed and clean), skip to Step 3 — the file is already on master and only Pages needs syncing.

---

## Step 2 — Commit to master

```bash
git add output/mag-buy-list.html
git commit -m "Update mag buy list report"
git push origin master
```

---

## Step 3 — Deploy to GitHub Pages

The `gh-pages` branch contains only `index.html`. Copy the current report there and push.

```powershell
Copy-Item "output\mag-buy-list.html" "$env:TEMP\pages-update.html"
git checkout gh-pages
Copy-Item "$env:TEMP\pages-update.html" "index.html" -Force
git add index.html
git commit -m "Deploy to Pages"
git push origin gh-pages
git checkout master
```

---

## Step 4 — Confirm

Tell the user the report is live at:
**https://hazyicestudios.github.io/VA-PreBan-MagBuyList/**

Note: GitHub Pages can take 1–2 minutes to reflect the update after pushing.
