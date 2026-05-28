# Reasoning: Game Concept — Dharma Duel CG

This document captures the thinking behind the prompt. It exists so a reader can understand not just *what* the prompt is, but *why* it ended up this way.

## Goal

Design a Top Trumps–style card game using Buddhist figures from ancient India. The format was chosen because it's universally familiar — players can pick it up without instructions, keeping the focus on the content (Buddhist history) rather than the rules. The intended use case was primarily as a teaching tool: something that could be used with students, novices, or community members to make Buddhist history engaging and memorable.

## Iteration history

This is the foundational prompt that launched the project. No prior version existed. The initial concept was stated in a single sentence: "A Top Trump inspired card game during the time of Buddha in Ancient India." The extended product/process/performance description that followed was drafted collaboratively to lock in scope before any code was written. The character list (40 figures across 10 archetypes) was researched during the session by the user, drawing on Buddhist knowledge.

## Failure modes the final version handles

The scoping session deliberately prevented scope creep — by separating deliverables (JSON data, card.py, game.py, ui.py, docs) and defining an iterative release model (v1 prototype → v1.1 polish → v1.2+ features), the project avoided the common failure of trying to build everything at once. The character list was also scoped to figures with clear textual backing in the Pali Canon, preventing the roster from expanding into obscure or disputed figures.

## Outcome

A complete v1.0 prototype was generated: working source files, 39-card JSON database, fact files and stories on every card, traditional Top Trumps mechanics. The prototype was good enough to iterate from; the project ran all the way to v2.9 from this foundation.

## What I'd change next

In hindsight, committing the character list to a spreadsheet for review before coding it into JSON would have saved some rework — individual Five Ascetics cards were later removed and Añña Kondañña was re-added as a separate card. A structured "card design review" step before code generation would be worth adding to future game projects.

## Tags

`game-design` `project-init` `content-generation` `buddhist-history`
