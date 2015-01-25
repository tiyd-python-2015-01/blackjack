"""
Interface
    Responsibilities:
        -Accept user input
        -Output appropriate text
    Collaborators
        -Game
"""
from .player import Player
from .player import Dealer


class Interface:
    def __init__(self):
        pass

    def welcome(self):
        """ Welcome screen.  Recursively called Yes_or_No asking if user
        wants to play. """
        print("""\n\nWelcome to the game of blackjack!""")
        print("""Would you like to play a game?""")
        return self.yes_or_no()

    def print_options(self):
        """ Allows user to set shoe size.  More options can be added. """
        print("""Would you like to choose the size of the shoe?""")
        options = self.yes_or_no()
        if str(options) == "quit":
                return "quit"
        elif options:
            return self.get_shoe_size()
        else:
            return 1

    def get_shoe_size(self):
        """ User enters shoe size.  get_shoe_input validates user input. """
        print("Great!\nPlease enter a size between 1 and 8.")
        return self.get_shoe_input()

    def get_bet(self, max_bet):
        """ Prompts user to place a bet.  Returns validated amount. """
        if max_bet > 1:
            print("How much would you like to bet?  $1 - {}".format(max_bet))
        else:
            print("You've got one dollar left.  Make it worth it!")
            return 1
        return self.get_bet_input(max_bet)

    def display_hands(self, player, dealer):
        """ Shows all player's cards and all but one dealer card.
        Player is left justified, Dealer is 30 characters to the right.
        Player's assessed value is printed at bottom. """
        player_hand = player.display_hand()
        dealer_hand = dealer.display_hand()
        max_length = max(len(player_hand), len(dealer_hand))
        print("Your Hand:".ljust(30), "Dealer Hand".ljust(30))
        for n in range(0, max_length):
            try:
                print(str(player_hand[n]).ljust(30),
                      str(dealer_hand[n]).ljust(30))
            except:
                try:
                    print(str(player_hand[n]).ljust(30))
                except:
                    print(" ".ljust(30), str(dealer_hand[n]).ljust(60))
        print("Your Value: {}".format(player.assess_hand()).ljust(30), "\n")
        return "{}\n{}".format(player_hand, dealer_hand)

    def player_wins(self, player):
        """ Player wins, shows current cash. """
        print("You win!", "\n")
        self.players_pot(player)

    def player_loses(self, player):
        """ Player loses, shows current cash. """
        print("You lose.", "\n")
        self.players_pot(player)

    def player_ties(self, player):
        """ Player ties, shows current cash. """
        print("Game is a push.", "\n")
        self.players_pot(player)

    def players_pot(self, player):
        """ Shows current cash. """
        print("You currently have ${}".format(player.cash), "\n")

    def hit_or_stand(self):
        """ Asks user if they want another card. """
        print("Another Card?")
        return self.yes_or_no()

    def dealer_hits(self, dealer, player):
        """ Dealer hits.  Show current cards. """
        print(" ".ljust(30), "Dealer hits:")
        self.display_hands(player, dealer)

    def dealer_stands(self, dealer, player):
        """ Dealer stands.  Show current cards. """
        print(" ".ljust(30), "Dealer stands")
        self.display_hands(player, dealer)

    def play_again(self):
        """ Asks user to play again. """
        print("Would you like to play again?")
        return self.yes_or_no()

    def busted(self):
        """ Printed if player busts. """
        print("You've busted.")
        print("Game over.\n")

    def final_cards(self, player, dealer):
        """ Same as display_cards but shows ALL of dealer's hand and dealer's
        hand's value. """
        player_hand = player.display_hand()
        dealer_hand = dealer.display_entire_hand()
        max_length = max(len(player_hand), len(dealer_hand))
        print("Your Hand:".ljust(30), "Dealer Hand".ljust(30))
        for n in range(0, max_length):
            try:
                print(str(player_hand[n]).ljust(30),
                      str(dealer_hand[n]).ljust(30))
            except:
                try:
                    print(str(player_hand[n]).ljust(30))
                except:
                    print(" ".ljust(30), str(dealer_hand[n]).ljust(60))
        print(("Your Value: {}".format(player.assess_hand()).ljust(30)),
              ("Dealer Value: {}".format(dealer.assess_hand()).ljust(30)),
              "\n")
        return "{}\n{}".format(player_hand, dealer_hand)

    def farewell(self, player):
        """ End of game. Console a player with no money."""
        print("Thanks for playing!")
        print("You're leaving with ${}".format(player.cash))
        if player.cash < 1:
            print("Maybe tomorrow will be better!")

    def get_bet_input(self, max_bet, try_count=1):
        """Validates if bet is number and less than player's cash.
        Recursively calls itself upon bad input and
        returns 10 after three tries"""
        if try_count > 3:
            # Defaults to $10 bets if user enters bad input.
            # However, if user doesn't have $10, make them bet everything.
            if max_bet >= 10:
                return 10
            else:
                return max_bet
        bet = input(">>")
        try:
            if 0 < int(bet) <= max_bet:
                return int(bet)
            else:
                return self.get_bet_input(max_bet, try_count+1)
        except:
            if bet == "quit":
                return "quit"
            else:
                return self.get_bet_input(max_bet, try_count+1)

    def get_shoe_input(self, try_count=1):
        """ Validates for a number 1-8.
        Recursively calls itself upon bad input and
        returns 1 after three recursive calls"""
        if try_count > 3:
            print("You've chosen 1 deck!")
            return 1
        size = input(">>")
        try:
            if 0 < int(size) <= 8:
                if size == 1:
                    print("You've chosen 1 deck!")
                else:
                    print("You've chosen {} decks!".format(size))
                return int(size)
            else:
                return self.get_shoe_input(try_count+1)
        except:
            if size == "quit":
                return "quit"
            else:
                return self.get_shoe_input(try_count+1)

    def yes_or_no(self):
        """ Validates input for a case insensitive 'yes','y','no', or 'n'
        Recursively calls itself upon bad input. """
        print("[Y]es")
        print("[N]o\n")
        answer = input(">>").lower()
        if answer == "y" or answer == "yes":
            return True
        elif answer == "n" or answer == "no":
            return False
        elif answer == "quit":
            return "quit"
        else:
            return self.yes_or_no()
