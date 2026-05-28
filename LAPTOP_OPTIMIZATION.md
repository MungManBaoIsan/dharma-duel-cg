# Laptop Screen Optimization

## Overview

Dharma Duel v2.0 is now **optimized for 14" laptop screens** while maintaining full functionality and readability.

---

## Screen Specifications

### Window Size
- **Resolution**: 1200 x 700 pixels
- **Fits**: 1366 x 768 (typical 14" laptop)
- **Margins**: 166px horizontal, 68px vertical
- **Scaling**: All elements proportionally scaled

### Previous (v1.0)
- **Resolution**: 1200 x 800 pixels
- **Issue**: Cards cut off on 14" screens
- **Required**: Scrolling or fullscreen

### Current (v2.0)
- **Resolution**: 1200 x 700 pixels
- **Result**: Everything visible without scrolling
- **Benefit**: Works on all laptop sizes

---

## What Fits On Screen

### Header Section (Top)
```
📚 20  ████████████░░░░░░  19 📚
YOUR STACK              OPPONENT STACK
Rounds: 5               Rounds: 3
```
- **Height**: 70 pixels
- **Always visible**: Card counts and progress
- **Clear indicators**: Who's winning

### Card Display Area
```
┌──────────────┐    ┌──────────────┐
│  Your Card   │    │ Opp. Card    │
│  360x580     │    │  360x580     │
│              │    │              │
│  All content │    │  All content │
│  visible     │    │  visible     │
└──────────────┘    └──────────────┘
```
- **Card size**: 360 x 580 pixels (down from 400 x 650)
- **Gap**: 80 pixels between cards
- **Position**: Y = 100 (leaves room for header)

### Bottom Margin
- **Space**: 20 pixels
- **Purpose**: Visual breathing room

---

## Scaling Details

### Fonts Scaled Down

| Element | v1.0 | v2.0 | Usage |
|---------|------|------|-------|
| Title | 48pt | 42pt | Menu screens |
| Header | 36pt | 32pt | Card names |
| Stat | 28pt | 24pt | Turn indicator |
| Text | 22pt | 20pt | Stats, facts |
| Small | 18pt | 16pt | Archetype, story |

### Card Components Scaled

| Section | v1.0 | v2.0 | Savings |
|---------|------|------|---------|
| Card width | 400px | 360px | -40px |
| Card height | 650px | 580px | -70px |
| Name spacing | 40px | 30px | -10px |
| Stat height | 40px | 34px | -6px each |
| Story spacing | 25px | 22px | -3px |

**Total height saved**: ~90 pixels

---

## Visual Elements Optimized

### Progress Bar
- **Width**: 300px → 250px (more compact)
- **Height**: 30px → 25px
- **Border**: 3px → 2px
- **Position**: Centered at top

### Card Stacks Indicator
- **Icon**: 📚 emoji (universal symbol)
- **Size**: 32pt (large and visible)
- **Labels**: "YOUR STACK" / "OPPONENT STACK"
- **Spacing**: Compact but clear

### Stat Buttons
- **Height**: 35px → 30px
- **Font**: 28pt → 24pt
- **Padding**: Reduced by 2px
- **Still clickable**: Easy to click

---

## Readability Maintained

### Text Legibility
✅ **All text readable** at normal viewing distance  
✅ **Font sizes appropriate** for laptop screens  
✅ **Good contrast** (dark on light backgrounds)  
✅ **No eyestrain** with extended play  

### Information Hierarchy
✅ **Card counts prominent** (largest text with icons)  
✅ **Card names clear** (bold, good size)  
✅ **Stats readable** (medium font)  
✅ **Stories legible** (smaller but clear)  

### Interactive Elements
✅ **Stat buttons easily clickable** (30px height)  
✅ **Hover effects work well** (clear feedback)  
✅ **Progress bar visible** (250px wide)  

---

## Testing Results

### Tested Resolutions

| Resolution | Result | Notes |
|------------|--------|-------|
| 1366 x 768 | ✅ Perfect | Standard 14" laptop |
| 1440 x 900 | ✅ Perfect | Some 15" laptops |
| 1600 x 900 | ✅ Perfect | Larger laptops |
| 1920 x 1080 | ✅ Perfect | Full HD (extra space) |
| 1280 x 720 | ⚠️ Tight | Minimum recommended |

### What Works

✅ **No scrolling needed**  
✅ **All content visible**  
✅ **Cards fully rendered**  
✅ **Text readable**  
✅ **Progress bar clear**  
✅ **Gameplay smooth**  

---

## Benefits

### Accessibility
- **Works on more devices** (14" and up)
- **No external monitor needed**
- **Portable gaming** on laptops

### User Experience
- **See everything at once** (no scrolling)
- **Track progress easily** (card stacks always visible)
- **Better focus** (compact layout)

### Performance
- **Smaller window** (less rendering)
- **Faster drawing** (fewer pixels)
- **Better on older laptops**

---

## Layout Breakdown

```
Screen: 1200x700

┌────────────────────────────────────────────────┐ 0px
│              PROGRESS BAR & STACKS             │
│  📚 20  ████████████░░░░░░  19 📚              │ 70px
├────────────────────────────────────────────────┤
│                                                │
│  ┌──────────────┐    ┌──────────────┐        │
│  │  Your Card   │    │ Computer     │        │
│  │  360x580     │    │ Card         │        │
│  │              │    │ 360x580      │        │
│  │              │    │              │        │
│  │  • Name      │    │ • Name       │        │
│  │  • Archetype │    │ • Archetype  │        │
│  │  • Facts     │    │ • Facts      │        │
│  │  • Stats     │    │ • Stats      │        │
│  │  • Story     │    │ • Story      │        │
│  │              │    │              │        │
│  └──────────────┘    └──────────────┘        │ 680px
│                                                │
└────────────────────────────────────────────────┘ 700px
```

---

## Future Enhancements

Potential improvements:
- **Responsive scaling** for different screen sizes
- **Fullscreen mode** toggle
- **Adjustable font sizes** in settings
- **Window resizing** support

---

## System Requirements

### Minimum
- **Display**: 1280 x 720 (tight but works)
- **OS**: Windows, Mac, Linux
- **Python**: 3.8+
- **Pygame**: 2.5.2+

### Recommended
- **Display**: 1366 x 768 or higher
- **OS**: Any modern OS
- **Python**: 3.10+
- **Pygame**: 2.6+

### Optimal
- **Display**: 1920 x 1080
- **Extra space**: Better visual breathing room
- **Still compact**: Uses same window size

---

**Version**: 2.0  
**Optimized for**: 14" Laptop Screens  
**Window Size**: 1200 x 700  
**Status**: Fully tested and working

🙏
