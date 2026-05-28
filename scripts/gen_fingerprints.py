import json, re

test_cases = [
    ("game-concept", "What files does the Dharma Duel project scaffold include?"),
    ("game-concept", "What characters are included in the Dharma Duel card game?"),
    ("card-database-design", "Describe the Angulimala card in the database"),
    ("card-database-design", "Describe the Sujata card"),
    ("stat-system-redesign", "What is Angulimala merit score and why?"),
    ("stat-system-redesign", "Why was Mythic Significance replaced with Merit?"),
    ("archetype-naming", "What is Angulimala archetype and legend status?"),
    ("archetype-naming", "What is the difference between Khema and Visakha archetypes?"),
    ("game-mechanics", "Explain how the turn system works when a player wins a round"),
    ("game-mechanics", "Explain what happens when both cards tie on the selected stat"),
    ("balance-tuning", "What are Buddha final stats and overall rating?"),
    ("balance-tuning", "Which card can beat Buddha on Influence?"),
    ("ai-and-ui-features", "Describe the Easy AI mode strategy mix"),
    ("ai-and-ui-features", "Describe the card viewer ranking feature"),
]

for prompt, inp in test_cases:
    inputs = {"input": inp}
    s = json.dumps(inputs, sort_keys=True)
    fp = re.sub(r'\W+', '_', s)[:60]
    print(f"{prompt} | {fp}")
