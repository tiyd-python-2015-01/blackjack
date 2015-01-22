from deck import Deck

class Dealer:

    def __init__(self):

        self.hand = []

    def get_hand(self, deck):
        self.hand.append(deck.get_card())
        self.hand.append(deck.get_card())

    def __len__(self):
        return len(self.hand)

    def hit(self, deck):
        self.hand.append(deck.get_card())
