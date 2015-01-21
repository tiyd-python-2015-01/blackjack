import random
from card import Card
my_deck = []

class Deck:
    card_suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
    card_numbers = ["2","3","4","5","6","7","8","9","10", "ACE",
                    "KING","QUEEN","JACK"]
## self.cards[0..52] = Card(number,suit) deck = Deck(...)    deck = Deck(...)
#deck.cards[]



    def generate_cards():
        card_suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
        card_numbers = ["2","3","4","5","6","7","8","9","10", "ACE",
                        "KING","QUEEN","JACK"]
        for suit in card_suits:
            for number in card_numbers:
                if number in ["KING","QUEEN","JACK"]:
                    value = 10
                elif number == "ACE":
                    value = 1,11
                else:
                    value = int(number)
                card = Card(number, suit,value)
                my_deck.append(card)

Deck.generate_cards()

print(len(my_deck))
