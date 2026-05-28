# Development Journal — Dharma Duel Card Game
A chronological log of key developments, decisions and learnings throughout this project.

---

## 28 May 2026 — Shipped to GitHub and Itch.io

**Type:** Milestone

**What I built or did**

I took the Dharma Duel Card Game and shipped it publicly — from files on my computer to a live, downloadable game.

Here's what got done:
- Created a public GitHub repo at `MungManBaoIsan/dharma-duel-cg` with 16 curated files — the game code, card database, documentation, and launchers
- Fixed a PyInstaller bundling bug so the Windows executable could find its card data after packaging
- Built a self-contained Windows `.exe` (14.6 MB) using Python 3.12
- Got the game live on Itch.io at `mungmanbaoisan.itch.io/dharma-duel-cg`

**Why I did it this way**

I chose Itch.io over Render because Dharma Duel is a desktop game, not a web app — Render hosts servers, Itch.io hosts downloadable games. The GitHub repo was deliberately curated: the original folder had 20+ internal dev-process markdown files. I kept only the 16 files that add value to someone reading the repo.

**How it works**

The key technical step was the PyInstaller fix. When Python is bundled into a single `.exe`, the `__file__` variable no longer points to the project root — it points inside a temporary folder. I added a `_resource_path()` helper that uses `sys._MEIPASS` (PyInstaller's bundled data directory) when available, so `data/cards.json` loads correctly whether you're running from source or from the executable.

**What this means for the app**

Dharma Duel is now publicly available. Anyone can download and play it without installing Python. The GitHub repo is clean and presentable for employers or anyone curious about the code.

**What I learned**

Render and Itch.io solve different problems — and assuming "deployment" always means Render sent me in the wrong direction at first. Adjusting once the actual target was clear was straightforward, but it was a useful reminder to match the tool to the problem, not the habit.

The PyInstaller `__file__` path issue is a common gotcha: the fix is simple once you know it exists, but without that knowledge the app silently fails to find its card data after packaging.

**How We Did It**

1. Scanned the project folder and decided which 16 files to include (excluded 20+ dev-process docs)
2. Initialised git and created the GitHub repo via `gh repo create`
3. Spotted the PyInstaller path bug in `card.py`, fixed it, committed
4. Built the Windows `.exe` using Python 3.12 (Python 3.14 doesn't yet support Pygame)
5. Packaged the executable into a zip for Itch.io
6. Guided the Itch.io page setup — title, player-focused description, upload, tags, publish
7. Confirmed the repo was fully up to date with all final v2.9 changes

**References / Conversations**

Session with Claude Code (claude-sonnet-4-6), 28 May 2026. Skills used: `portfolio-update`, `dev-journal`, `tone-profile`.

---
