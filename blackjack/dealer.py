from hand import Hand


class Dealer:

    """
    Responsibilities:
    Decide to hit or stay,
    keeps track of a hand of cards.

    Collaborates with: Deck.
    """

    def __init__(self):
        self.hand = Hand()
        self.face_down = Hand()

    def reveal(self):
        """When it becomes the dealers turn he will reveal the facedown card."""
        face_down_card = self.face_down.remove()
        self.hand.add(face_down_card)

    def take_card(self, deck):
        """Gives the dealer the ability to draw cards from the deck."""
        card = deck.deal_card()
        self.hand.add(card)

    def put_face_down(self, deck):
        """Lets the dealer draw a card and put it facedown."""
        card = deck.deal_card()
        self.face_down.add(card)

    def __str__(self):
        return "The dealers hand consists of {}".format(self.hand)

    def __repr__(self):
        return self.__str__()
