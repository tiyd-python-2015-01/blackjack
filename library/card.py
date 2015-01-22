class Card:
    """A card is a component of a deck of cards. There are 52 card types.

    Responsibilities:
    A card has one suit, from the set of {Diamonds, Spades, Hearts, Clubs}.
    A card has a distinct value from the set {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                                              Jack, Queen, King}
    A card has a blackjack value of (1-10) or is an ace, which is either 1 or
    11, whichever is more expedient to the posessor's hand

    Collaborators:
    Cards are initially contained in a deck.
    Cards are also put into hands.
    """
    def __init__(self, suit, rank):
        suit = suit
        rank = rank


    def rank_print(self):
        if rank == "Jack":
            return "J"
        elif rank == "Queen":
            return "Q"
        elif rank == "King":
            return "K"
        else:
            return rank


    def __str__(self):
        return "{}{}".format(self.suit[0], self.rank_print())


    def __repr__(self):
        return self.__str__
