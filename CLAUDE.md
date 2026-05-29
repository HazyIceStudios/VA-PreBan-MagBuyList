# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Context

* Virginia law banning the sale of high-capacity magazines and certain firearms takes effect **July 1, 2026** (~34 days away)
* The law allows grandfathered ownership of items purchased before the ban takes effect
* Goal: stock up on magazines and firearms before the deadline to preserve legal grandfathered status
* All outputs and recommendations must account for legal compliance


## Rules

* Always use plan mode
* Always ask clarifying questions before starting a complex task
* Always prompt for repository name when creating a new repository


## Project Structure

* `workflows/` — Workflow instruction files (**not yet created**)
* `output/` — Finished deliverables (**not yet created**)
* `resources/` — Reference docs, templates, and data

**Note:** `workflows/` and `output/` directories do not exist yet; do not assume they are populated.


## Data Files

* `resources/Pistol Mag Sheet.csv` — Despite the `.csv` extension, this is an **Excel `.xlsx` file** and must be handled accordingly (e.g., use openpyxl or pandas with the xlsx engine, not plain CSV parsing)


## Repository Status

* This project is **not yet a git repository** — do not run git commands without first initializing one


## GitHub

* https://github.com/HazyIceStudios
