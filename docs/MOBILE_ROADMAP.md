# Mobile Version — Future Roadmap

The browser version works well on desktop and tablet (landscape). It doesn't work well on phones because the game was built at 1440×840 — a desktop resolution. Making it properly mobile-friendly is a significant project.

## Why it's hard

- The game renders at a fixed 1440×840 resolution internally (in `ui.py`)
- All card layout, font sizes, button positions, and spacing are hardcoded to that resolution
- The game uses mouse click detection — phones use touch events
- Portrait mode on a phone gives nowhere near enough horizontal space for the card layout

## What a proper mobile version needs

### 1. Responsive resolution
- Detect the screen size at startup and scale the layout to fit
- `pygame.display.get_surface().get_size()` gives the actual canvas size at runtime
- All positions and sizes in `ui.py` would need to use relative values (e.g. `screen_width * 0.1`) instead of fixed pixel numbers

### 2. Portrait-mode layout
- The current layout is landscape-first (two cards side by side)
- Portrait needs a stacked layout: player card on top, opponent card below, stats in the middle
- This is essentially a new screen layout — a significant redesign of `ui.py`

### 3. Touch support
- Pygame handles touch events via `pygame.FINGERDOWN` and `pygame.FINGERUP`
- The current code only listens for `pygame.MOUSEBUTTONDOWN`
- Pygbag (the browser runtime) maps touch to mouse events on some devices, but not reliably

### 4. Font sizes
- Many fonts will be too small to read on a 390px-wide phone screen
- All font sizes in `ui.py` would need to scale with screen size

## Suggested approach when ready

1. Start with the web version folder (`dharma_duel_web/`)
2. Add screen-size detection to `ui.py __init__`
3. Build a portrait layout as a separate draw path (keep landscape working)
4. Test with browser dev tools (Chrome → Toggle device toolbar → iPhone view)
5. Rebuild the pygbag package and re-upload to Itch.io

## Files to focus on

- `dharma_duel_web/ui.py` — all layout and rendering (main work)
- `dharma_duel_web/main.py` — event loop (add touch event handling here)
- `dharma_duel_web/build/web/index.html` — pygbag config (`fb_width`, `fb_height`, viewport meta)

## Estimated effort

This is a medium-to-large task. Expect 2–4 sessions of focused work. It's a good portfolio project because responsive game design is a real skill.
