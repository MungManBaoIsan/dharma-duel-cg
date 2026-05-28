from card import CardDeck

deck = CardDeck()
print(f"\nTotal cards: {len(deck.cards)}\n")
for i, card in enumerate(deck.cards, 1):
    print(f"{i}. {card.name}")