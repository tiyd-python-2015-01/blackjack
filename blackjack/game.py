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

    def create_hands(self):
        dealer_cards = []
        player_cards = []
        for _ in range(2):
            player_cards.append(self.deck.deal())
            dealer_cards.append(self.deck.deal())
        self.player.hands.append(Hand(player_cards))
        self.dealer.hand = Hand(dealer_cards)
