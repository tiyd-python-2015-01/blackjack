class Player:
    """The player of the blackjack game.

    Responsibilities:

    * Holds a hand
    * Can bet
    * Can hit

    Collaborators:

    *Uses a hand of cards
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = [x for x in hand.hand]

    def hit(self, deck):
        card = deck.draw()
        self.hand.append(card)
