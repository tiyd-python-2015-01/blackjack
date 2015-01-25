import random
from card import Card, ranks, suits


class Deck:
    """A shuffled deck of playing cards.

    Responsibilities:
    *Constructs a shuffled deck containing 1 of each card.
    *Allows cards to be drawn
    *Should be able to report it's current size
    collaborators:
    +Collects 1 of each card from the Card class.
    """
    def __init__(self):
        self.cards = []
        for rank in ranks:
            for suit in suits:
                card = Card(rank, suit)
                self.cards.append(card)
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return " ".join([card.__str__() for card in self.cards])

    def __eq__(self, other):
        return self.__cards__ == other.__cards__
