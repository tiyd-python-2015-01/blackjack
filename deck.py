import random
from card import Card

class Deck:

    def __init__(self):
        self.my_deck = []

        card_suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
        card_numbers = ["2","3","4","5","6","7","8","9","10", "Ace",
                        "King","Queen","Jack"]
        for suit in card_suits:
            for number in card_numbers:
                if number in ["King","Queen","Jack"]:
                    value = 10
                elif number == "Ace":
                    value = 1,11
                else:
                    value = int(number)
                card = Card(number, suit,value)
                self.my_deck.append(card)

    def get_length(self):
        return len(self.my_deck)

    def __str__(self):
        return str(self.my_deck)

    def get_card(self):
        rand_card = self.my_deck.pop(random.randint(0,len(self.my_deck)-1))
        print(rand_card)
        return rand_card
"""
new_deck = Deck()
print(new_deck.get_length())
new_deck.get_card()
print(new_deck.get_length())

"""
