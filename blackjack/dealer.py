class Dealer:
    """
    Responsibilities:
    Decide to hit or stay,
    keeps track of a hand of cards.

    Collaborates with: Deck.
    """
    def __init__(self):
        self.hand = Hand()
        self.hidden_hand = Hand()

    def reveal(self):
        hidden_card = self.hidden_hand.pop()
        self.hand.append(hidden_card)
