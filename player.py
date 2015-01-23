from hand import Hand


class Player:
    """The player of the blackjack game.

    Responsibilities:

    * Holds a hand
    * Can bet
    * Can hit
    * Can display hand

    Collaborators:

    *Uses a hand of cards
    """
    def __init__(self, name, stack = 0, hand = Hand([])):
        self.name = name
        self.hand = hand
        self.cards = hand.hand
        self.stack = stack


    def hit(self, deck):
        card = deck.draw()
        return self.cards.append(card)


    def bet(self, amount):
        chips = self.stack
        new_chips = chips - amount
        self.stack = new_chips
        return self.stack


    def show_hand(self):
        print("{name}'s hand: {hand}".format(name = self.name, hand = self.hand))
