from hand import Hand


from player import Player

class Dealer():
    """The dealer of the blackjack game. The dealer doesn't actually deal
    cards, but holds a hand for the purpose of the game.

    Responsibilities:

    * Holds a Hand of Cards
    * Hits until 17 or more, if over 21 returns bust
    * Has facedown card

    Collaborators

    * Gets a hand of cards from the deck
    """

    def __init__(self, hand = Hand([])):
        self.name = "Dealer"
        self.hand = hand
        self.cards = hand.hand

    def hit(self, deck):  #change to hand class
        card = deck.draw()
        return self.cards.append(card)

    def play_out_hand(self, deck):
        while self.hand.soft_total < 17:
            self.hit(deck)
