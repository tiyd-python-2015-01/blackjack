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

    def __init__(self, hand = None):
        if hand == None:
            hand = Hand([])
        self.name = "Dealer"
        self.hand = hand


    def hit(self, deck):
        self.hand.draw(deck)


    def play_out_hand(self, deck):
        while self.hand.soft_total < 17:
            if self.hand.hard_total >= 17 and self.hand.hard_total <= 21:
                return self.hand.hard_total
                break
            self.hand.draw(deck)
        return self.hand.soft_total

    def show_hand(self):
        print("{name}'s hand: XX {hand}".format(name = self.name, hand = self.hand.hand[1]))

    def reveal_hand(self):
        print("{name}'s hand: {hand} ({value})".format(name = self.name,
                                               hand = self.hand,
                                               value = self.hand.best_hand))
