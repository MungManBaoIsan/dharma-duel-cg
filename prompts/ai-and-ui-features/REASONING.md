# Reasoning: AI Difficulty Levels and UI Features

## Goal

Build an AI opponent that feels human rather than robotic, and add UI features that made the game both accessible (card viewer with rankings, difficulty selection) and thematically rich (Dharmachakra wheel card back, Dharma Council story).

## Iteration history

**AI v1 — Always picks highest stat:** Correct but boring after a few games. Completely predictable — players memorise that the computer will always choose the stat it's strongest at.

**AI v2 — Smart mode (60/30/10):** The 60/30/10 split (60% top-2 stats / 30% middle stats / 10% weak stats) was introduced to make the AI feel human. The 10% mistake rate is deliberate — it means experienced players can occasionally out-think the AI on a round, which is satisfying without making the AI feel incompetent.

**AI v3 — 4 difficulty levels:** Expanded to Easy/Moderate/Hard/Smart to serve different audiences:
- Easy (20/30/50): Beginners win reliably; good for teaching Buddhist history in a classroom or monastery setting
- Moderate (40/40/20): A fair contest for casual play
- Hard (85/10/5): Near-optimal; a real challenge for experienced players
- Smart (60/30/10): The "human feel" mode; most fun for replayability

The dual motivation: accessibility for beginners + human-feeling play for experienced players. These are two separate needs that one AI mode cannot serve.

**Card viewer — rankings:** The card viewer originally had 8 sort options (ID, Name, and each stat). Adding a "Ranking" sort showing cards 1–40 by overall rating gave players a complete map of the deck's power hierarchy. This was useful both for strategy (knowing which cards you're holding relative to the deck) and for learning (understanding where each figure ranks within the tradition).

**Story — Sāgara replaced by Dharma Council:** The original story opened with statistics about Buddhism's global decline from 5% to 4% of world population. This was thematically honest but wrong in tone for a card game. Nobody wants to open a battle game with melancholic sociological data. The replacement does two things simultaneously: sets up the game premise (40 legendary beings, mystical tournament, you are summoned) and energises players to play. A story that doesn't connect to what you're about to do is wasted screen real estate.

**Dharmachakra wheel:** The "?" text character was a placeholder. Replacing it with actual drawn graphics (8 spokes for the Eightfold Path, hub, outer rim, decorative dots) served both purposes: thematic depth (the hidden card contains teachings, like the Dharma itself) and visual quality (the card back is seen constantly, so it should be beautiful). The text character was capped by font size; the drawn wheel fills the card face and looks deliberately designed.

## Failure modes the final version handles

- Predictable single-AI mode (4 difficulty levels solve this)
- No way to assess deck composition before playing (card viewer + ranking solve this)
- Story tone mismatch for a game context (Dharma Council framing solves this)
- Generic placeholder card back (drawn Dharmachakra wheel solves this)

## Outcome

Four working AI modes. Card viewer with 9 sort options including full ranking 1–40. Story reader accessible from main menu with complete Dharma Council narrative. Dharmachakra wheel rendered as Pygame graphics — 8 spokes, hub, decorative dots, gold on dark brown.

## What I'd change next

Sound effects on card reveal and a slow-spinning Dharmachakra animation on the card back would significantly increase the feeling of polish.

## Tags

`game-design` `code-generation` `content-generation` `ui`
