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
    def __init__(self, *args):
        self.cards = []
        for arg in args:
            self.cards.append(arg)

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

    def value(self):
        value_dict = {"1": 11,
                      "2": 2,
                      "3": 3,
                      "4": 4,
                      "5": 5,
                      "6": 6,
                      "7": 7,
                      "8": 8,
                      "9": 9,
                      "10": 10,
                      "Jack": 10,
                      "Queen": 10,
                      "King": 10}

        initial_value = 0
        for card in self.cards:
            initial_value += value_dict[card.rank]
        return initial_value

    def can_split(self):
        return len(self.cards) == 2 and self.cards[0].same_rank(self.cards[1])
