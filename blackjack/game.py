from deck import Deck
from hand import Hand
from player import Player
from dealer import Dealer


class Game:
    """ This is the main game class.  It provides an interface for interaction
    between the deck, player and dealer.  It receives rule options from the
    game options class to properly initialize the dealer to play with the
    selected ruleset and properly initialize the deck to have the selected
    number of cards.

    Responsibilites:
    * Initializes the deck for play
    * Initializes the dealer
    * Keeps track of the player's wager
    * Resolves whether the dealer of player wins a hand

    Collaborators:
    * Interacts with the deck class to generate a deck of the correct size
    * Interacts with the GameOptions class to determine the ruleset for the
      game and initialize the dealer appropriately
    * Receives wager from player and transfers winnings to player"""


    def __init__(self, options, name):
        self.deck = Deck(options.number_of_decks)
        self.player = Player(name)
        self.dealer = Dealer(options.hit_soft_17)
        self.options = options

    def can_split(self, hand):
        if self.options.split_by_rank:
            if hand.get_ranks()[0] == hand.get_ranks()[1]:
                return True
            else:
                return False
        else:
            if hand.get_values()[0] == hand.get_values()[1]:
                return True
            else:
                return False
                
    def create_hands(self):
        dealer_cards = []
        player_cards = []
        for _ in range(2):
            player_cards.append(self.deck.deal())
            dealer_cards.append(self.deck.deal())
        self.player.hands.append(Hand(player_cards))
        self.dealer.hand = Hand(dealer_cards)

    def check_bust(self, hand):
        if hand.get_value() > 21:
            return True
        else:
            return False

    def check_push(self, hand1, hand2):
        if hand1.get_value() == hand2.get_value():
            return True
        else:
            return False

    def compare_hands(self, player_hand, dealer_hand ):
        if player_hand.get_value > dealer_hand.get_value:
            return True
        else:
            return False
