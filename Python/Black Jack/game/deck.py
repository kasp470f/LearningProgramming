def deckGen():
    cards = [ "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A" ]
    suits = [ "♠", "♣", "♥", "♦" ]

    deck = []

    for x in suits:
        for y in cards:
            deck.append(y+x)
    return deck