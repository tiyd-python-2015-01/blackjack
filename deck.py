import card
import random

class Deck:

    def __init__(self):
        self.deck = [card.Card(number,suit) for suit in card.card_suits for number
                     in card.card_numbers]

    def get_length(self):
        print(len(self.deck))
        return len(self.deck)

    def __str__(self):
        return str(self.my_deck)

    def get_card(self):
        rand_card = self.deck.pop(random.randint(0,len(self.deck)-1))
        print(rand_card)
        return rand_card
