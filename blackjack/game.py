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

    def can_double(self, hand):
        """Checks to see if the option to double down is abailable to the
        player"""
        if self.options.no_double_after_split and len(self.player.hands) > 1:
            return False
        else:
            if self.options.double_9_10_11:
                return 9 <= hand.get_value() < 12 and len(hand.cards) == 2
            elif self.options.double_9_10:
                return 9 <= hand.get_value() < 11 and len(hand.cards) == 2
            else:
                return len(hand.cards) == 2

    def can_hit(self, hand):
        """Checks to see if the player has the option to hit.  Only not
        available if hitting split aces is disabled and player has split
        aces"""
        if not self.options.hit_split_aces and (len(self.player.hands) > 1
            and hand.cards[0].rank == "A"):
            return False
        else:
            return True

    def can_split(self, hand):
        """Checks to see if the option to split is available to the player"""
        if not self.options.resplitting and len(self.player.hands) > 1:
            return False
        elif not self.options.resplit_aces and (len(self.player.hands) > 1
            and "A" in hand.get_ranks()):
            return False
        elif self.options.split_by_rank:
            return hand.get_ranks()[0] == hand.get_ranks()[1]
        else:
            return hand.cards[0] == hand.cards[1]

    def can_surrender(self, player_hand, dealer_show_card):
        """Checks to see if the options to surrender is available to the
        player"""
        return (not self.options.no_surrender
                and len(player_hand.cards) == 2
                and dealer_show_card.rank == "A")

    def create_hands(self, bet):
        """Creates the player and dealer hands and assigns them to their
        respective objects"""
        dealer_cards = []
        player_cards = []
        for _ in range(2):
            player_cards.append(self.deck.deal())
            dealer_cards.append(self.deck.deal())
        self.player.hands.append(Hand(bet, player_cards))
        self.dealer.hand = Hand(0, dealer_cards)

    def check_bust(self, hand):
        """Checks to see if a hand has busted"""
        return hand.get_value() > 21

    def check_push(self, player_hand, dealer_hand):
        """Compares a player and dealer hand and to see if a set of hands
        results in a push state"""
        return player_hand.get_value() == dealer_hand.get_value()

    def compare_hands(self, player_hand, dealer_hand ):
        """Compares the player and dealer hand to resolve the winner"""
        return player_hand.get_value > dealer_hand.get_value

    def takes_hit(self, hand):
        hand.add_cards(self.deck.deal())

    def splits(self, hand):
        self.player.modify_money(-1 * hand.bet)
        new_hand = Hand(hand.bet, [hand.cards[1], self.deck.deal()])
        hand.cards.pop(1)
        hand.add_cards(self.deck.deal())
        self.player.hands.append(new_hand)

    def doubles(self, hand):
        self.player.modify_money(-1 * hand.bet)
        hand.bet *= 2
        self.takes_hit(hand)
