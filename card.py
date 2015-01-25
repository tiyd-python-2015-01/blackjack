suits = ['♡', '♢', '♧', '♤']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Card:
    """Playing card.

    Responsibilities:

    *Card has a rank, suit and value derived from the rank.
    *Two cards with same rank and suit should be equal to eachother

    Collaborators:

    *Collected in a Deck
    *Collected in a Hand for the players and a Hand for the dealer.
    """
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        if self.rank.isdigit():
            self.value = int(self.rank)
        elif self.rank is 'A':
            self.value = 1
        else:
            self.value = 10

    def __eq__(self, other):
        """Test equality for 2 cards."""
        return self.suit == other.suit and self.rank == other.rank

    def __str__(self):
        return'{}{}'.format(self.rank, self.suit)
