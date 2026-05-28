# Dharma Duel - Deployment & Development Guide

## 🚀 How to Launch for Others to Play

You have several options for sharing your game with others:

### Option 1: Share the Source Code (Easiest for Tech-Savvy Users)
**Best for:** Friends/testers who are comfortable with Python

**Steps:**
1. Share the `dharma_duel_cg_v2.9_FINAL.zip` file
2. Users extract the zip
3. Users install Python 3.8+ and pygame:
   ```bash
   pip install pygame
   ```
4. Users run:
   ```bash
   python main.py
   ```

**Pros:**
- ✅ Simple to share
- ✅ Works on Windows, Mac, Linux
- ✅ Easy to update (send new zip)

**Cons:**
- ❌ Requires Python installation
- ❌ Technical barrier for non-programmers

---

### Option 2: Create Standalone Executable (Recommended)
**Best for:** Anyone who wants a simple double-click experience

**Using PyInstaller:**

#### Windows Executable
```bash
# Install PyInstaller
pip install pyinstaller

# Navigate to game directory
cd dharma_duel_cg

# Create Windows .exe (on Windows)
pyinstaller --onefile --windowed --name "DharmaDuel" main.py

# Executable will be in: dist/DharmaDuel.exe
```

#### Mac App Bundle
```bash
# On Mac
pyinstaller --onefile --windowed --name "DharmaDuel" main.py

# Creates: dist/DharmaDuel.app
```

#### Linux Binary
```bash
# On Linux
pyinstaller --onefile --name "DharmaDuel" main.py

# Creates: dist/DharmaDuel
```

**Important:** Include the `data/` and `assets/` folders with the executable!

**Distribution Structure:**
```
DharmaDuel/
├── DharmaDuel.exe (or .app or binary)
├── data/
│   └── cards.json
└── assets/
    ├── fonts/
    └── images/
```

**Pros:**
- ✅ No Python installation needed
- ✅ Professional feel
- ✅ Easy for users to run
- ✅ Can distribute as zip

**Cons:**
- ❌ Must create separate builds for Windows/Mac/Linux
- ❌ Larger file size

---

### Option 3: Web Version (Most Accessible)
**Best for:** Maximum reach, no installation

**Using Pygame-Web (Pygbag):**

```bash
# Install pygbag
pip install pygbag

# Build web version
pygbag dharma_duel_cg

# Upload to GitHub Pages, itch.io, or your website
```

**Hosting Options:**
- GitHub Pages (free)
- itch.io (free, game-focused)
- Your own website

**Pros:**
- ✅ No installation needed
- ✅ Works on any device with browser
- ✅ Easiest to share (just send link)
- ✅ Automatic updates

**Cons:**
- ❌ Requires web hosting
- ❌ Some Pygame features may need adjustments

---

### Option 4: Publish on Itch.io (Recommended for Distribution)
**Best for:** Reaching gamers, getting feedback, building audience

**Steps:**
1. Create account at https://itch.io
2. Click "Upload New Project"
3. Choose options:
   - **Downloadable:** Upload your executable + files as zip
   - **Browser Playable:** Upload web version
   - **Pay What You Want:** Set price (can be free)
4. Add description, screenshots, tags
5. Publish!

**Pros:**
- ✅ Built for game distribution
- ✅ Community features
- ✅ Free hosting
- ✅ Analytics
- ✅ Can accept donations

**Cons:**
- ❌ Requires creating account
- ❌ Some setup time

---

### Option 5: GitHub Releases (Best for Open Source)
**Best for:** Open source development, version tracking

**Steps:**
1. Create GitHub repository
2. Push your code:
   ```bash
   git init
   git add .
   git commit -m "Initial release v2.9"
   git remote add origin https://github.com/yourusername/dharma-duel.git
   git push -u origin main
   ```
3. Create Release:
   - Go to Releases → New Release
   - Tag: v2.9
   - Upload `dharma_duel_cg_v2.9_FINAL.zip`
   - Upload executables (Windows/Mac/Linux)
4. Share release link

**Pros:**
- ✅ Version control
- ✅ Professional
- ✅ Free hosting
- ✅ Easy to track issues
- ✅ Community contributions

**Cons:**
- ❌ Requires Git knowledge
- ❌ Public by default (can use private repo)

---

## 🛠️ Can You Still Develop After Launch?

**YES! Absolutely!** Here's how:

### Development Workflow

#### Setup
```
Your Development Environment:
├── dharma_duel_dev/         ← Your working version
│   ├── main.py
│   ├── game.py
│   ├── ui.py
│   └── data/cards.json
│
└── releases/
    ├── v2.9/                ← Released version
    └── v3.0/                ← Future release
```

#### Workflow
1. **Keep developing** in your main directory
2. **Test changes** thoroughly
3. **Create new release** when ready
4. **Share updated version** with users

---

### Version Control Best Practices

#### Using Git (Recommended)
```bash
# Work on new features in branches
git checkout -b feature/new-cards
# Make changes...
git commit -m "Added 10 new cards"

# When ready to release
git checkout main
git merge feature/new-cards
git tag v3.0
git push --tags

# Create new release on GitHub
```

#### Simple Version System (Without Git)
```
Keep dated backups:
├── dharma_duel_2024_12_06/  ← Current work
├── dharma_duel_2024_12_05/  ← Yesterday's backup
└── releases/
    ├── v2.9_2024_12_06/     ← Released to public
    └── v3.0_2025_01_15/     ← Next release
```

---

### Release Strategy

#### Version Numbering
```
v2.9    ← Current
v2.9.1  ← Bug fix (small changes)
v2.10   ← New features (medium changes)
v3.0    ← Major update (big changes)
```

#### Release Cycle Example
```
Week 1-2: Develop new features
Week 3: Testing and bug fixes
Week 4: Release v3.0
         Players download and play v3.0
         You continue developing v3.1
```

#### Changelog
Keep a CHANGELOG.md:
```markdown
# Changelog

## [v3.0] - 2025-01-15
### Added
- 10 new legendary cards
- Sound effects
- Card animations

### Fixed
- Menu navigation bug

## [v2.9] - 2024-12-06
### Added
- 4 AI difficulty levels
- Pass & Play mode improvements
```

---

### Development While Players Use Current Version

**The Key:** Separate your development work from released versions

```
Players are playing:     You are developing:
v2.9 (stable)           v3.0 (in progress)
                        ├── Testing new features
                        ├── Adding sound effects
                        └── Fixing bugs

When v3.0 is ready:
├── Release v3.0
├── Players download update
└── You start v3.1
```

---

## 🎯 Recommended Launch Strategy for You

Based on your project, here's what I recommend:

### Phase 1: Soft Launch (Now)
```
1. Share source code with close friends/testers
   - Send dharma_duel_cg_v2.9_FINAL.zip
   - Get feedback

2. Create GitHub repository
   - Track changes
   - Accept bug reports
   - Professional presence
```

### Phase 2: Executable Build (Next Week)
```
1. Create Windows .exe with PyInstaller
2. Test on different computers
3. Share with wider circle
4. Gather feedback
```

### Phase 3: Public Launch (When Ready)
```
1. Polish based on feedback
2. Create executables for Windows/Mac/Linux
3. Upload to itch.io
4. Share on Reddit, social media
5. Get community feedback
```

### Phase 4: Ongoing Development
```
1. Continue adding features
2. Release updates every 1-2 months
3. Build player community
4. Consider web version for accessibility
```

---

## 📦 Quick Start: Create Executable Now

### Windows Users
```bash
# Install PyInstaller
pip install pyinstaller

# Navigate to game folder
cd dharma_duel_cg

# Create executable
pyinstaller --onefile --windowed --name "DharmaDuel" --add-data "data;data" --add-data "assets;assets" main.py

# Find executable in: dist/DharmaDuel.exe
```

### Mac Users
```bash
pip install pyinstaller
cd dharma_duel_cg
pyinstaller --onefile --windowed --name "DharmaDuel" --add-data "data:data" --add-data "assets:assets" main.py

# Find app in: dist/DharmaDuel.app
```

### Create Distribution Zip
```bash
# Create folder structure
mkdir DharmaDuel_v2.9
cp dist/DharmaDuel.exe DharmaDuel_v2.9/  # or .app on Mac
cp -r data DharmaDuel_v2.9/
cp -r assets DharmaDuel_v2.9/
cp README.md DharmaDuel_v2.9/

# Create zip
zip -r DharmaDuel_v2.9_Windows.zip DharmaDuel_v2.9/
```

Share this zip file - users just extract and double-click!

---

## 🐛 Development Tips

### Testing Changes
```python
# Add debug mode to your game
DEBUG = True  # Set to False for releases

if DEBUG:
    print(f"Card: {card.name}, Stats: {card.stats}")
```

### Separate Development Branch
```
main branch    → Released versions (stable)
develop branch → Your active development (testing)
feature/X      → Specific new features
```

### Version Detection
```python
# Add to main.py
VERSION = "2.9"
RELEASE_DATE = "2024-12-06"

# Display in menu
print(f"Dharma Duel v{VERSION}")
```

---

## 🎓 Learning Resources

### PyInstaller
- Documentation: https://pyinstaller.org/
- Tutorial: Create executables for any platform

### Itch.io
- Creator docs: https://itch.io/docs/creators/
- Upload guide: https://itch.io/docs/creators/upload

### Git & GitHub
- Git basics: https://git-scm.com/book/en/v2
- GitHub releases: https://docs.github.com/en/repositories/releasing-projects-on-github

### Pygame Distribution
- Pygbag (web): https://pygame-web.github.io/
- Pygame docs: https://www.pygame.org/docs/

---

## ✅ Summary

### Can you launch now? **YES!**
- Share source code immediately
- Create executable in ~10 minutes
- Upload to itch.io in ~30 minutes

### Can you still develop? **YES!**
- Keep your development version separate
- Release updates when ready
- Players download new versions
- You control the pace

### Recommended Path:
1. **Now:** Share source with testers
2. **This week:** Create executable, share wider
3. **Next week:** Polish, upload to itch.io
4. **Ongoing:** Develop v3.0 while v2.9 is out

**You have full control over both development and distribution!**

🎮 Ready to launch! 🚀
