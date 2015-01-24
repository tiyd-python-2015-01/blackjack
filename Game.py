from dealer import Dealer
from player import Player
from hand import Hand
from card import Card
from deck import Deck, Clubs, Diamonds, Hearts, Spades


class Game:
    """Information about the game.

    Responsibilities:

    * Check for winner
    * Handles betting and bankroll
    * Resets the game and hands

    Collaborators

    * Checks the player and dealer's hand amounts and compares them
    """

    def __init__(self, dealer, player, deck):
        self.dealer = dealer
        self.player = player
        self.deck = deck
        self.pot = 0

    def play_again(self):
        choice = input('Press "p" to play again or "q" to quit: ').lower()
        return choice == 'p'


    def hit_or_stand(self):
        choice = input('Press "h" to Hit, or "s" to stand: ').lower()
        return choice == 'h'

    def new_turn(self):
        self.dealer.hand.reset_hand()
        self.player.hand.reset_hand()
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer.hand.new_hand(self.deck)
        self.player.hand.new_hand(self.deck)
        self.pot = 0

    def place_bet(self, amount):
        try:
            int(amount)
            if int(amount) <= self.player.stack:
                self.player.stack -= int(amount)
                self.pot += int(amount)
            else:
                self.place_bet(input("Not enough funds! You have {} dollars. "
                                     "Place a bet: ".format(self.player.stack)))
        except ValueError:
            self.place_bet(input("Place a bet: "))
