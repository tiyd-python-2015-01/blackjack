"""
Game
    Responsibilities:
        -Communicate the Game_State to Interface
        -Communicate the Interface to Game_State
        -Allow Players (Human & Dealer) to effect Game_State
        -Allow Game_State to effect Players (ie, deal cards)
        -Control game flow (ie, whose turn it is, end of game)
    Collaborators
        -Game_State
        -Interface
        -Players
"""
from .interface import Interface
from .player import Player
from .player import Dealer
from .carddeckshoe import Card
from .carddeckshoe import Deck
from .carddeckshoe import Shoe


class Game:


    def __init__(self):
        """The only three attributes of game are the user, dealer, shoe and
        interface.  Everything else is re-declared and initialized each time
        through the game loop."""
        self.user = Player()
        self.dealer = Dealer()
        self.interface = Interface()


    def start_game(self):
        """Print the Welcome Test and if the player accepts, begin loop."""
        if self.interface.welcome():
            return self.game_loop()
        else:
            return False

    def game_loop(self):
        """Initialize the Shoe and begin the loop:
            -Deal Cards
            -Check for blackjacks
            -Allow user to hit/stand
            -Perform hits/stands for dealer
            -Determine winner
            -Prompt player for another game """
        shoe_size = self.interface.print_options()
        self.shoe = Shoe(shoe_size)
        self.shoe.shuffle()
        while True:
            #If shoe gets down to last 20-25 cards, re-shuffle
            if len(self.shoe.cards) < 26:
                self.shoe = Shoe(shoe_size)
                self.shoe.shuffle()
            self.deal_cards()
            #self.show_cards()
            self.interface.display_hands(self.user,self.dealer)
            self.user.is_blackjack()
            self.dealer.is_blackjack()
            while (not self.user.is_blackjack()
                    and not self.user.busted()
                    and self.player_hit_or_stand()):
                self.user.get_card(self.shoe.give_card())
                #self.interface.show_cards(self.user)
                self.interface.display_hands(self.user,self.dealer)
            while (not self.user.busted()
                    and not self.dealer.busted()
                    and self.dealer.hit_or_stand()):
                self.dealer.get_card(self.shoe.give_card())
                self.interface.dealer_hits(self.dealer,self.user)
            else:
                self.interface.dealer_stands(self.dealer,self.user)
            self.win_or_lost()
            if not self.interface.play_again():
                self.interface.farewell(self.user)
                return False

    def win_or_lost(self):
        """ Print the final state of each hand
        Check for win, loss or push in order of importance.
        1. If user busted  2. If player busted  3. If player's hand is best
        4. If tie on 21, blackjack wins else push 5. push   """
        self.interface.final_cards(self.user,self.dealer)
        if self.user.busted():
            return self.player_loses(self.user)
        if self.dealer.busted():
            return self.player_wins(self.user)
        if self.user.assess_hand() > self.dealer.assess_hand():
            return self.player_wins(self.user)
        elif self.user.assess_hand() < self.dealer.assess_hand():
            return self.player_loses(self.user)
        elif self.user.assess_hand() == 21:
            if self.user.is_blackjack() and not self.dealer.is_blackjack():
                return self.player_wins(self.user)
            elif self.dealer.is_blackjack() and not self.user.is_blackjack():
                return self.player_loses(self.user)
            else:
                return self.player_ties(self.user)
        else:
            return self.player_ties(self.user)

    def player_loses(self,player):
        """ Deduct cash and print. """
        self.user.cash -= 10
        self.interface.player_loses(self.user)

    def player_wins(self,player):
        """ Reward cash and print. """
        self.user.cash += 10
        self.interface.player_wins(self.user)

    def player_ties(self,player):
        """ Print. """
        self.interface.player_ties(self.user)

    def deal_cards(self):
        """ Give both user and dealer a new hand of cards. """
        self.user.get_hand(self.shoe.deal_hand())
        self.dealer.get_hand(self.shoe.deal_hand())

    def show_cards(self):
        """ Show user and dealer's hands.  Dealer hides one card. """
        self.interface.display_hands(self.user, self.dealer)

    def player_hit_or_stand(self):
        """ Prompts player to hit or stand. """
        return self.interface.hit_or_stand()

    def dealer_hit_or_stand(self):
        """ Prints dealer's decision to hit or stand. """
        return self.interface.dealer_hit_or_stand()
