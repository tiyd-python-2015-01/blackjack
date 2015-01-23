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
        value_dict = {"1": 1,
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

        hand_value = 0
        ace_list = [card.is_ace() for card in self.cards]
        for card in self.cards:
            hand_value += value_dict[card.rank]
        if hand_value < 12 and any(ace_list):
            hand_value += 10
        return hand_value

    def has_ace(self):
        ace_list = [card.is_ace() for card in self.cards]
        return any(ace_list)

    def can_split(self):
        return len(self.cards) == 2 and self.cards[0].same_rank(self.cards[1])

    def is_bust(self):
        return self.value() > 21

    def show_cards(self, just_one=False):
        if just_one:
            return str(self.cards[0])
        else:
            card_list = [str(card) for card in self.cards]
            return card_list
