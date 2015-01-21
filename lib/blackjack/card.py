class Card:
    """Playing card class.  Each instance represents a single playing card.

    Responsibilities:

    * Each card has a string name attribute corresponding to it's value
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
             "hearts": "♡",
             "clubs": "♧",
             "diamonds": "♢"}

    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
        self.__evaluate_card_value__()

    def __str__(self):
         return self.name + self.suits[self.suit]

    def __repr__(self):
        return self.__str__()

    def __evaluate_card_value__(self):
        if self.name.isdigit():
            self.value = int(self.name)
        elif self.name == "A":
            self.value = 11
        else:
            self.value = 10

    def swap_ace(self):
        if self.value == 11:
            self.value = 1
        else:
            self.value = 11
