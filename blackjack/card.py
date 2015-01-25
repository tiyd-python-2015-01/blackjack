suits = ["hearts", "spades", "clubs", "diamonds"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9",
         "10", "J", "Q", "K"]


class Card:
    """Playing card class.  Each instance represents a single playing card.

    Responsibilities:

    * Each card has a string rank attribute corresponding to it's value
    * Each card has a suit attribute
    * Each card has a value determined by the private evaluate_card_value
      method
    * Ace value defaults to 11 but can be changed to 1 by calling the
      swap_ace method.

    Collaborators:

    * Cards are collected into decks of varying sizes
    * Cards are distributed to player and dealer hands
    """
    suits = {"spades": "♤",
             "hearts": "\033[.31m♡\033[.37m",
             "clubs": "♧",
             "diamonds": "\033[.31m♢\033[.37m"}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self._evaluate_card_value()

    def __str__(self):
        return self.rank + self.suits[self.suit]

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.value == other.value

    def _evaluate_card_value(self):
        """Evaluates the value of the card and sets it as a class attribute"""
        if self.rank.isdigit():
            self.value = int(self.rank)
        elif self.rank == "A":
            self.value = 11
        else:
            self.value = 10

    def swap_ace(self):
        """Swaps the value of the ace if requested by the game."""
        if self.value == 11:
            self.value = 1
        else:
            self.value = 11
