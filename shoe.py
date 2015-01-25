from deck import Deck


class Shoe():
    """Gathers the deck(s) into a shoe.

    *Contains the draw() method to draw from a concatenated list of decks.

    Collaborators:
    +Collects decks into a shoe.
    """

    def __init__(self):
        self.total = Deck().cards
        self.drawn_cards = []

    def __str__(self):
        return " ".join([cards.__str__() for cards in self.total])

    def set(self, n):
        """Method to determine the number of decks (n) in the shoe."""
        self.total *= n
        return self.total

    def draw(self):
        """Take a new card from the shoe and return it."""
        new_card = self.total.pop()
        self.drawn_cards.append(new_card)
        return new_card
