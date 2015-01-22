class Player:
    """
    Responsibilities:
    Has a hand and can accept cards into that hand.
    Should have a way of signeling hit or stay.

    Collaborates with:
    Deck.
    """
    def __init__(self):
        self.hand = []


    def __str__(self):
        return "Your hand consists of {}.".format(self.hand)


    def __repr__(self):
        return self.__str__()


    def take_card(self, card):
        self.hand.append(card)
        return self.hand
