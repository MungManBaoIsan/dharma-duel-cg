# 🎮 Dharma Duel for Windows & Mac Users

## 🚀 3 Ways to Get Dharma Duel on Windows/Mac

You have **3 excellent options**. Choose what works best for you!

---

## ✅ Option 1: Run with Python (Easiest - Works Now!)

**This is actually super simple!** Just 3 steps:

### **For Windows Users:**

#### Step 1: Install Python
1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or newer
3. **IMPORTANT:** Check ☑️ "Add Python to PATH" during installation
4. Click "Install Now"

#### Step 2: Install Pygame
Open Command Prompt and type:
```bash
pip install pygame
```

#### Step 3: Run the Game
1. Extract `dharma_duel_cg_v2.9_FINAL.zip`
2. Double-click `run_game.bat`

**That's it!** The game launches!

**Alternative:** Open Command Prompt in the game folder:
```bash
python main.py
```

---

### **For Mac Users:**

#### Step 1: Install Python
1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or newer
3. Install normally

#### Step 2: Install Pygame
Open Terminal and type:
```bash
pip3 install pygame
```

#### Step 3: Run the Game
1. Extract `dharma_duel_cg_v2.9_FINAL.zip`
2. Double-click `run_game.sh`

**That's it!** The game launches!

**Alternative:** Open Terminal in the game folder:
```bash
python3 main.py
```

---

## 🤖 Option 2: Automated Builds with GitHub Actions (Free!)

**Build executables for ALL platforms automatically - no Windows/Mac needed!**

### How It Works:
1. You push code to GitHub
2. GitHub's servers automatically build:
   - Windows .exe
   - Mac .app
   - Linux binary
3. You download all three ready-to-share!

### Setup (10 minutes):

#### Step 1: Create GitHub Account
Go to https://github.com and sign up (free!)

#### Step 2: Create Repository
1. Click "New Repository"
2. Name it: "dharma-duel"
3. Make it Public
4. Click "Create Repository"

#### Step 3: Upload Your Code
```bash
# On your computer (Linux):
cd dharma_duel_cg
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/dharma-duel.git
git push -u origin main
```

#### Step 4: Create Release
1. In GitHub, click "Releases" → "Create a new release"
2. Tag: `v2.9`
3. Title: `Dharma Duel v2.9`
4. Click "Publish release"

#### Step 5: Wait for Builds (5-10 minutes)
GitHub Actions automatically:
- ✅ Builds Windows .exe
- ✅ Builds Mac .app
- ✅ Builds Linux binary
- ✅ Attaches all to your release!

#### Step 6: Download & Share
Your release now has 3 downloadable files:
- `DharmaDuel_Windows.zip`
- `DharmaDuel_Mac.zip`
- `DharmaDuel_Linux.zip`

**Share one link - works for everyone!**

### Pros:
- ✅ Free automated builds
- ✅ Build for platforms you don't own
- ✅ Professional distribution
- ✅ Version control included
- ✅ One link for all platforms

---

## 💻 Option 3: Build Executables Yourself

If you have access to Windows/Mac computers, build locally:

### **On Windows Computer:**

```bash
# Install tools
pip install pygame pyinstaller

# Build executable
cd dharma_duel_cg
pyinstaller dharma_duel.spec

# Find it in: dist/DharmaDuel.exe
```

**Package for distribution:**
```bash
mkdir DharmaDuel_v2.9_Windows
copy dist\DharmaDuel.exe DharmaDuel_v2.9_Windows\
xcopy /E data DharmaDuel_v2.9_Windows\data\
xcopy /E assets DharmaDuel_v2.9_Windows\assets\
copy PLAYER_GUIDE.md DharmaDuel_v2.9_Windows\README.txt
```

Right-click folder → Send to → Compressed folder

---

### **On Mac Computer:**

```bash
# Install tools
pip3 install pygame pyinstaller

# Build executable
cd dharma_duel_cg
pyinstaller dharma_duel.spec

# Find it in: dist/DharmaDuel.app
```

**Package for distribution:**
```bash
mkdir DharmaDuel_v2.9_Mac
cp -r dist/DharmaDuel.app DharmaDuel_v2.9_Mac/
cp -r data DharmaDuel_v2.9_Mac/
cp -r assets DharmaDuel_v2.9_Mac/
cp PLAYER_GUIDE.md DharmaDuel_v2.9_Mac/README.txt
zip -r DharmaDuel_v2.9_Mac.zip DharmaDuel_v2.9_Mac/
```

---

## 🎯 Which Option Should You Choose?

### **Choose Option 1 (Python) if:**
- ✅ You want to share immediately
- ✅ Users are okay installing Python (2 minutes)
- ✅ You want the simplest approach
- ✅ Users will run from source

**Result:** Users double-click `run_game.bat` (Windows) or `run_game.sh` (Mac)

---

### **Choose Option 2 (GitHub Actions) if:**
- ✅ You want executables for ALL platforms
- ✅ You don't own Windows/Mac computers
- ✅ You want automated builds
- ✅ You want professional distribution

**Result:** Three .zip files, users extract and double-click to play!

---

### **Choose Option 3 (Build Locally) if:**
- ✅ You have Windows/Mac access
- ✅ You want full control
- ✅ You want to build manually
- ✅ You prefer not using GitHub

**Result:** Platform-specific executables you build yourself

---

## 📦 What Users Get with Each Option

### Option 1 (Python):
```
User downloads: dharma_duel_cg_v2.9_FINAL.zip (126 KB)
User installs: Python + Pygame (5 minutes)
User runs: Double-click run_game.bat or run_game.sh
Works: ✅ Windows, Mac, Linux
```

### Option 2 (GitHub Actions):
```
User downloads: 
  - DharmaDuel_Windows.zip (35 MB) - for Windows
  - DharmaDuel_Mac.zip (35 MB) - for Mac
  - DharmaDuel_Linux.zip (34 MB) - for Linux
User installs: Nothing!
User runs: Extract and double-click
Works: ✅ Specific platform only
```

### Option 3 (Manual Build):
```
Same as Option 2, but you build manually on each platform
```

---

## 🎮 Recommended Strategy

### **Right Now (Today):**
**Share Python version** with Windows/Mac users:
1. Send them `dharma_duel_cg_v2.9_FINAL.zip`
2. Send them this guide
3. They install Python + Pygame
4. They run `run_game.bat` (Windows) or `run_game.sh` (Mac)

**Pros:** Available immediately, works perfectly, small download

---

### **This Week:**
**Set up GitHub Actions** for automated builds:
1. Create GitHub repository
2. Upload your code
3. Create release tag
4. Download built executables
5. Share with everyone!

**Pros:** Professional, executables for all platforms, no Python needed

---

### **Future:**
**Upload to itch.io** with all platforms:
1. Upload Windows, Mac, Linux builds
2. One link works for everyone
3. Users choose their platform
4. Download and play!

**Pros:** Easiest for users, looks professional, builds community

---

## 📋 Quick Comparison

| Method | Setup Time | User Install | File Size | Platforms | Best For |
|--------|------------|--------------|-----------|-----------|----------|
| **Python** | 0 min | 5 min | 126 KB | All | Immediate sharing |
| **GitHub Actions** | 10 min | 0 min | 35 MB | All | Professional |
| **Manual Build** | Varies | 0 min | 35 MB | Per build | Full control |

---

## ✅ What's Included

All options include:
- ✅ 40 legendary cards
- ✅ 4 AI difficulty levels
- ✅ Pass & Play mode
- ✅ Card viewer
- ✅ Story reader
- ✅ Full documentation
- ✅ Perfect balance

---

## 🎯 Your Action Plan

### **Today:**
1. Share source code with Windows/Mac friends
2. Include launcher scripts (`run_game.bat`, `run_game.sh`)
3. They install Python and play immediately!

### **This Week:**
1. Set up GitHub repository
2. Enable GitHub Actions
3. Get automated builds for all platforms

### **Next Month:**
1. Upload to itch.io
2. Share one link
3. Works for everyone!

---

## 💡 Pro Tips

### **For Windows Users:**
The `run_game.bat` script:
- ✅ Checks if Python is installed
- ✅ Installs Pygame if needed
- ✅ Launches the game
- ✅ Shows helpful errors

Just double-click it!

### **For Mac Users:**
The `run_game.sh` script:
- ✅ Checks if Python 3 is installed
- ✅ Installs Pygame if needed
- ✅ Launches the game
- ✅ Shows helpful errors

Just double-click it!

### **For Everyone:**
Python installation is quick (2-5 minutes) and then the game runs perfectly!

---

## 🆘 Common Questions

**Q: Do users really have to install Python?**
A: Only if using Option 1. Options 2 & 3 give them executables with no install needed. But Python install is actually very quick and easy!

**Q: Is Python installation hard?**
A: No! Just download from python.org, check one box, click install. 2 minutes.

**Q: Can I use GitHub Actions without knowing Git?**
A: Yes! GitHub has a web interface. Upload files through browser, click buttons to create releases.

**Q: How long do GitHub Actions builds take?**
A: About 5-10 minutes to build all 3 platforms automatically.

**Q: Which option is best?**
A: **Option 1 for immediate sharing, Option 2 for professional distribution!**

---

## 🎉 Summary

### **Windows Users Can:**
1. Run with Python (super easy!) ← **Recommended for now**
2. Wait for executable (GitHub Actions build)
3. Get manual build if you have Windows PC

### **Mac Users Can:**
1. Run with Python (super easy!) ← **Recommended for now**
2. Wait for executable (GitHub Actions build)
3. Get manual build if you have Mac

### **You Can:**
1. Share Python version **today** ✅
2. Set up GitHub Actions **this week** ✅
3. Get executables **automatically** ✅
4. Share with **everyone** ✅

---

**🚀 Windows & Mac users are covered! Multiple great options! 🚀**

**Share the Python version now, build executables later!**

**🎮⚡🖥️🍎✨👍🎯**
