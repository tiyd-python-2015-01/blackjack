from card import Card, ranks, suits


class Hand:
    """Contains the value for a given hand and the Ace exception rule.

    *Determines the value of a given hand from the rank of each card
    *Implements the ace swap if a card is an ace and the hand value < 12.

    Collaborators:
    +Collects Cards.
    """

    def __init__(self):
        self.cards = []
        self.value = 0

    def __str__(self):
        return ' '.join([str(card) for card in self.cards])

    def get_value(self):
        """Determines the value of the current hand."""
        self.value = 0
        for card in self.cards:
            self.value += card.value
        for card in self.cards:
            if card.rank == 'A' and self.value < 12:
                self.value += 10
        if len(self.cards) == 2 and self.value == 21:
            return 'BLACKJACK'
        else:
            return self.value
