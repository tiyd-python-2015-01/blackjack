import card
import random


class Deck:

    def __init__(self):
        self.deck = [card.Card(number, suit) for suit in card.card_suits for
                     number in card.card_numbers]

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        return str(self.my_deck)

    def get_card(self):
        return self.deck.pop(random.randint(0, len(self.deck)-1))
