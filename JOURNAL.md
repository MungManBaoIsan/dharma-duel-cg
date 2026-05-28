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

## 28 May 2026 — Added a Prompt Library to Document the Whole Build

**Type:** Milestone

**What I built or did**

I added a `/prompts` folder to the Dharma Duel repo that documents every major design decision made during the project — from the first game concept right through to the AI difficulty system.

Seven prompts are archived, each with:
- The actual prompt used (verbatim, in a fenced block)
- A `REASONING.md` explaining *why* the decision was made
- A `rubric.yaml` with testable pass/fail criteria
- Version history for prompts that were iterated (e.g. the turn system went through 7 versions)

The eval runner (`scripts/eval_runner.py`) checks all 7 rubrics automatically. All pass at 100% using mock fixtures, with no API costs. GitHub Actions runs this on every push.

**Why I did it this way**

This came out of a structured exercise: instead of just building, I documented the *thinking* behind the decisions. It makes the repo useful as portfolio evidence — a recruiter or collaborator can read `prompts/README.md` in 90 seconds and understand not just what was built, but how design problems were solved.

**How it works**

The skill (prompt-archivist) ran a seven-phase process:
1. Scan the project and conversation history
2. Interview me on each decision (7 chunks, one at a time)
3. Draft REASONING.md files and get approval before writing anything
4. Write all prompt artifacts to disk
5. Build the index (`prompts/README.md`) and `CHANGELOG.md`
6. Install the eval runner and confirm all rubrics pass
7. Add GitHub Actions CI workflow

**What this means for the app**

The repo now shows *how* the game was made, not just the result. The `game-mechanics` prompt documents 7 debugging iterations. The `stat-system-redesign` prompt shows why Mythic Significance was wrong and why Merit was right. The `balance-tuning` prompt shows the 10,000-game simulation that confirmed near-perfect odds.

**What I learned**

The most useful part of the process was the interview phase — being asked *why* for each decision forced me to articulate things I'd done instinctively. For example, I hadn't consciously framed the legend card decision as "rarity creates excitement" until the question asked me to justify it. That kind of reflection is the whole point of a portfolio.

**How We Did It**

1. Ran prompt-archivist skill — scanned project, identified 7 prompt chunks
2. Interviewed me on all 7 (format, card DB, stat redesign, archetypes, mechanics, balance, AI/UI)
3. Drafted REASONING.md for each chunk and got approval before writing files
4. Wrote all 21+ files (prompt.md, REASONING.md, rubric.yaml per prompt, plus versions/)
5. Built prompts/README.md index and CHANGELOG.md
6. Installed eval_runner.py, wrote 14 fixture files, debugged fingerprint mismatches
7. All 7 rubrics passing at 100% in mock mode
8. Committed 140 files, pushed to GitHub, merged with existing remote history

**References / Conversations**

Session with Claude Code (claude-sonnet-4-6), 28 May 2026. Skills used: `prompt-archivist`, `portfolio-update`.

---

## 29 May 2026 — Added Browser Version via pygbag

**Type:** Feature

**What I built or did**

Added a Play in browser option to the Itch.io page. The game now works both as a Windows download (.exe) and directly in the browser — no install needed.

**Why I did it this way**

Keeping the original `main.py` untouched was a priority. I created a separate `dharma_duel_web/` folder with copies of the 4 game files and a web-only `main.py` — the only difference is the game loop is `async` and yields each frame with `await asyncio.sleep(0)`, which is what pygbag (the browser conversion tool) requires.

**How it works**

pygbag packages the Python/Pygame code into WebAssembly — a format browsers can run directly. The Pygame runtime loads from a CDN on first visit (~20 second load time), then the game runs at full speed.

**What this means for the app**

Friends can now play instantly from the Itch.io link with no download. The .exe download is still there for better performance.

**What I learned**

The async change is minimal but must be in a separate entry point — touching the original `main.py` risks breaking the desktop version.

**How We Did It**

1. Created `dharma_duel_web/` — copies of card.py, game.py, ui.py, data/cards.json
2. Wrote web-only `main.py` with async game loop
3. Built with `python -m pygbag --build dharma_duel_web`
4. Zipped `build/web/` → `DharmaDuel_Browser.zip` (68KB)
5. Uploaded to Itch.io, ticked "Play in browser", set viewport 1200×700
6. Confirmed Play in browser button appears on game page

**References / Conversations**

Session with Claude Code (claude-sonnet-4-6), 29 May 2026. Skills used: `portfolio-update`.

---

## 29 May 2026 — Browser Version Working in Fullscreen

**Type:** Feature / Problem Solving

**What I built or did**

Got the browser version of Dharma Duel working cleanly on Itch.io. The Itch.io embed is now set to "Click to launch in fullscreen" so players get a great experience immediately with no fiddling.

**Why I did it this way**

Viewport tweaking alone couldn't solve the readability problem — results were inconsistent (too small, too vertical, too zoomed depending on the size chosen). The real fix was fullscreen mode, which lets the browser scale the game properly to whatever screen the player has.

**How it works**

The web copy (`dharma_duel_web/`) has its own `ui.py` with fonts and screen scaled up 20% (1440×840, fonts proportionally larger). Original files untouched. pygbag rebuilds from this folder only.

**What I learned**

When viewport tweaking produces inconsistent results, it's a sign the scaling approach is wrong — not that a bigger or smaller number is needed. Fullscreen sidesteps the problem entirely.

**How We Did It**

1. Tried Itch.io viewport size changes — too small, too vertical, too zoomed
2. Scaled web ui.py up 20% (screen, fonts, cards)
3. Rebuilt with pygbag, rezipped, re-uploaded to Itch.io
4. Discovered fullscreen mode looks great — set embed to "Click to launch in fullscreen"

**References / Conversations**

Session with Claude Code (claude-sonnet-4-6), 29 May 2026. Skills used: `portfolio-update`.

---
