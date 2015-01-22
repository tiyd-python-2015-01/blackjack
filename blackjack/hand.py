import card
import deck


class Hand:
    """A hand is a collection of cards held by a player or dealer.

    Resposibilities:
    A hand has a blackjack value, composed of the most favorable sum of its
    cards.
    A hand must be able to display part or all of its cards to the player.

    Collaborators:
    Hands recieve cards from decks.
    Hands are possesed and played by the player or the dealer.
    """
    def __init__(self):
        self.cards = []

    def grab(self, a_card):
        self.cards.append(a_card)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        if len(self.cards) == 0:
            return "[]"
        else:
            a_string = str(self.cards)
            return a_string

    def __repr__(self):
        return self.__str__()
