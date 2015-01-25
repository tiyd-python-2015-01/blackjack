import pickle
from game_options import GameOptions
from random import choice


icons = ["♡", "♧", "♢", "♤"]


class Interface:
    """ Interface class will provide all of the methods of interacting with
    the user.  It will contain all of the methods for displaying to the
    console as well as receiving and checking input from the player.

    Responsibilities:
    * Output game information and menus to the player
    * Receiving input from the player
    * Control game flow
    """

    def __init__(self):
        self.game = None

    def check_for_dealer_blackjack(self):
        """Checks the dealer's hand for blackjack"""
        return self.game.dealer.hand.get_value() == 21

    def check_for_player_blackjack(self):
        """Checks to see if the player has blackjack"""
        if (self.game.player.hands[0].get_value() == 21
                and len(self.game.player.hands[0].cards) == 2
                and len(self.game.player.hands) == 1):
            print("BLACKJACK!\n")
            if self.check_for_dealer_blackjack():
                print("Dealer has BLACKJACK.  Push...\n")
                self.game.payout(self.game.player.hands[0],
                                 self.game.dealer.hand)
                return True
            else:
                print("Blackjack pays 3:2!\n")
                self.game.payout_blackjack(self.game.player.hands[0])
                return True
        else:
            return False

    def dealer_play(self):
        """Dealer's play method.  Goes through all dealer turns until the
        hit() method of dealer determines it needs to stand or the dealer
        busts"""
        while self.game.dealer.hit():
            new_card = self.game.deck.deal()
            print("Dealer hits, and recieves {}.\n".format(str(new_card)))
            self.game.dealer.takes_hit(new_card)

        if self.game.check_bust(self.game.dealer.hand):
            print("Dealer busts!\n")
            for hand in self.game.player.hands:
                if hand.get_value() <= 21:
                    self.game.payout(hand, self.game.dealer.hand)
            return False
        else:
            return True

    def evaluate_hands(self):
        """Evaluates the final hands of the player and dealer and makes
        the appropriate calls the the playout method of the Game class"""
        if len(self.game.player.hands) > 1:
            self.evaluate_split_hands()
        elif self.game.check_push(self.game.player.hands[0],
                                  self.game.dealer.hand):
            self.game.payout(self.game.player.hands[0],
                             self.game.dealer.hand)
            print("Push.\n")
            self.print_dealer_hand()
        else:
            if self.game.compare_hands(self.game.player.hands[0],
                                       self.game.dealer.hand):
                print("You win!\n")
                self.game.payout(self.game.player.hands[0],
                                 self.game.dealer.hand)
                self.print_dealer_hand()
            else:
                print("Dealer wins.\n")
                self.print_dealer_hand()

    def evaluate_split_hands(self):
        """Method for evaluating multiple hands after a split."""
        for hand in enumerate(self.game.player.hands):
            if self.game.check_bust(hand[1]):
                print("Hand {} busted.".format(hand[0]+1))
            elif self.game.check_push(hand[1], self.game.dealer.hand):
                print("Push on hand {}.".format(hand[0]+1))
                self.game.payout(hand[1], self.game.dealer.hand)
            else:
                if self.game.compare_hands(hand[1], self.game.dealer.hand):
                    print("Hand {} wins!".format(hand[0]+1))
                    self.game.payout(hand[1], self.game.dealer.hand)
                else:
                    print("Hand {} loses!".format(hand[0]+1))
        self.print_dealer_hand()

    def execute_selection(self, selection, actions):
        """Takes the users selected action and performs it"""
        if selection == "H" and actions["hit"]:
            new_card = self.game.deck.deal()
            print("\nReceived {}\n".format(new_card))
            self.game.player.takes_hit(self.game.player.hands[
                                       self.current_hand],
                                       new_card)
        elif selection == "D" and actions["double"]:
            new_card = self.game.deck.deal()
            print("\nReceived {}\n".format(new_card))
            self.game.player.doubles(self.game.player.hands[self.current_hand],
                                     new_card)
        elif selection == "P" and actions["split"]:
            new_cards = [self.game.deck.deal(), self.game.deck.deal()]
            self.game.player.splits(self.game.player.hands[self.current_hand],
                                    new_cards)
        elif selection == "R" and actions["surrender"]:
            self.game.player.surrenders(self.game.player.hands[
                                        self.current_hand])

    def initialize_hand(self):
        """Initializes the variables needed for the correct flow of the
        hand"""
        print("\n"*80)
        bet = self.get_bet()
        print("\n"*80)

        self.game.player.reset_player()
        self.game.create_hands(bet)
        self.current_hand = 0
        self.dealers_turn = False
        self.continue_hand = True

        if len(self.game.deck.cards) < 30:
            self.game.reshuffle()

    def offer_actions(self):
        """Prints available actions to the screen and allows user to input
        their selected action."""
        actions = self.game.get_available_actions(
            self.game.player.hands[self.current_hand])
        valid_selection_made = False
        while not valid_selection_made:
            valid_input = ["S"]
            if actions["hit"]:
                print("(H)it, ", end="")
                valid_input.append("H")
            if actions["double"]:
                print("(D)ouble Down, ", end="")
                valid_input.append("D")
            if actions["split"]:
                print("S(P)lit, ", end="")
                valid_input.append("P")
            if actions["surrender"]:
                print("Surrende(R), ", end="")
                valid_input.append("R")
            print("(S)tand")
            selection = input("{} ".format(choice(icons))).upper()
            valid_selection_made = selection in valid_input

        return selection, actions

    def offer_insurance(self):
        """Method that allows the user to buy insurace if the dealer's upcard
        is an Ace"""
        print("Dealer has an Ace showing.  Buy insurance?")
        while True:
            player_choice = input("(Y/N) {} ".format(choice(icons))).upper()
            if player_choice == "Y":
                self.game.player.buys_insurance()
                break
            elif player_choice == "N":
                break
            else:
                print("Please enter Y or N.")

    def play_game(self, game):
        """Starts each hand an keeps the game going.  Offers the user the
        choice to play another hand or not."""
        self.game = game

        while self.game.player.money >= 5:
            self.play_hand()
            while True:
                if self.game.player.money < 5:
                    print("You don't have enough money to play!")
                    input()
                    break
                player_choice = input("Play another hand? (Y/N) {} ".format(
                                      choice(icons))).upper()
                if player_choice in ["Y", "N"]:
                    break
            if player_choice == "N" and self.game.player.money > 5:
                save_choice = ""
                while save_choice not in ["Y", "N"]:
                    save_choice = input(
                        "Would you like to save? (Y/N) {} ".format(
                            choice(icons))).upper()
                if save_choice == "Y":
                    self.game.player.save_player_state(self.game.options)
                    break
                else:
                    break

    def play_hand(self):
        """Hand loop.  Continues until the end of the hand.  Prints updates
        about the status of the hand to the screen and makes method calls
        to allow user actions."""

        self.initialize_hand()
        print("Dealing Cards {}\n".format(choice(icons)))

        while self.continue_hand:
            self.print_hands()

            if self.resolve_blackjacks():
                break

            selection, actions = self.offer_actions()
            self.execute_selection(selection, actions)

            dealers_turn = self.players_turn(selection)

            if dealers_turn:
                print("Dealer's turn!")
                need_to_compare = self.dealer_play()
                if need_to_compare:
                    self.evaluate_hands()
                    self.continue_hand = False
                else:
                    self.continue_hand = False

    def players_turn(self, selection):
        """Allows the player to make game selections and determines if the
        dealer will need to take a turn"""
        dealers_turn = False
        if self.game.check_bust(self.game.player.hands[self.current_hand]):
            if len(self.game.player.hands) == 1:
                print("You bust!\n")
                self.continue_hand = False
                return False
            elif len(self.game.player.hands) == self.current_hand + 1:
                print("You bust!\n")
                for hand in self.game.player.hands:
                    if hand.get_value() <= 21:
                        dealers_turn = True
                return dealers_turn
            else:
                print("You bust!\n")
                self.current_hand += 1
        elif selection == "R":
            print("You surrendered...\n")
            self.continue_hand = False
            return False
        elif selection == "S" or selection == "D":
            if len(self.game.player.hands) > self.current_hand + 1:
                self.current_hand += 1
            else:
                return True

    def print_dealer_hand(self):
        """Prints the dealer's hand to the screen"""
        print("Dealer's final hand: {}\n".format(
            self.game.dealer.hand.get_card_strings()))

    def print_hands(self):
        """Displays the dealer's and player's hands to the screen"""
        print("Dealer's Hand: [{}, [X]]".format(
              self.game.dealer.get_show_card()))

        print("Player's Hand{}: ".format("s" if len(self.game.player.hands) > 1
                                         else ""), end="")
        card_string = ""
        for hand in enumerate(self.game.player.hands):
            card_string += "{}{} ".format("*" if hand[0] == self.current_hand
                                          else "",
                                          hand[1].get_card_strings(), end="")

        print(card_string)
        print("\nMoney: {}".format(self.game.player.money))

    def resolve_blackjacks(self):
        """Resolves all cases of either or both the player and dealer having
        blackjack and makes appropriate payouts.  Also calls the offer
        insurance method to allow the player to insure before blackjacks
        are resolved."""
        if self.check_for_player_blackjack():
            return True
        if (self.game.dealer.get_show_card().rank == "A"
                and len(self.game.player.hands[0].cards) == 2
                and len(self.game.player.hands) == 1
                and self.game.player.money >= self.game.player.hands[0].bet):
            self.offer_insurance()
            if self.game.options.early_surrender:
                if self.offer_surrender():
                    self.game.player.surrenders(self.game.player.hands[0])
                    print("You surrendered.\n")
                    print("Dealer had: {}\n".format(
                        self.game.dealer.hand.get_card_strings()))
                    return True

        if self.check_for_dealer_blackjack():
            print("Dealer has blackjack!\n")
            self.game.payout(self.game.player.hands[0],
                             self.game.dealer.hand)
            return True

        return False

    def main_menu(self):
        """ Displays the title, programmer info, and main menu for the game.
        Takes user input and returns to the calling Game class"""
        title_text = ("\n"
                      ".------..------..------..------..------."
                      ".------..------..------..------.\n"
                      "|B.--. ||L.--. ||A.--. ||C.--. ||K.--. |"
                      "|J.--. ||A.--. ||C.--. ||K.--. |\n"
                      "| :(): || :/\: || (\/) || :/\: || :/\: |"
                      "| :(): || (\/) || :/\: || :/\: |\n"
                      "| ()() || (__) || :\/: || :\/: || :\/: |"
                      "| ()() || :\/: || :\/: || :\/: |\n"
                      "| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|"
                      "| '--'J|| '--'A|| '--'C|| '--'K|\n"
                      "`------'`------'`------'`------'`------'"
                      "`------'`------'`------'`------'")

        info = ("Programmed by: Alan Grissett\n"
                "The Iron Yard - Durham\n"
                "January 2015\n")

        menu_text = ("<><><><><><><><><><><><><><><><><><><><><><>"
                     "<><><><><><><><><><><><><><")

        print("\n"*80, menu_text)
        print(title_text)
        print("\n", menu_text)
        print(info)
        print("Main Menu:")
        print("♡ 1 - New Game")
        print("♤ 2 - Continue Game")
        print("♧ 3 - Set Game Options")
        print("♢ 4 - Quit")
        print("-----------------------")
        selection = input("{} ".format(choice(icons)))

        return selection

    def get_bet(self):
        """Prompts the user to select a bet amount in multiples of 5, not
        exceeding 20"""
        print("\n"*80)
        while True:
            print("How much would you like to wager on the next hand? ")
            print("Please wager in multiples of 5.  Maximum bet is 20.")
            try:
                print("Type \"O\" to go to the options menu.")
                print("You currently have {} dollars.".format(
                    self.game.player.money))
                bet = input("{} ".format(choice(icons)))
                if bet.upper() == "O":
                    self.options_menu(self.game.options)
                    continue
                bet = int(bet)
                if (bet % 5 is not 0
                        or bet < 0
                        or bet > 20
                        or bet > self.game.player.money):
                    raise ValueError
                else:
                    return bet
            except ValueError:
                print("Sorry, that's not a valid bet.")

    def get_name(self):
        """Prompts the user to input a name, used for the creation of a
        Player object."""
        print("\n"*80)
        print("Great!  Let's play some Blackjack!")
        name = input("Please enter your name {} ".format(choice(icons)))
        return name

    def options_menu(self, options):
        """Displays the options menu and updates option variables to reflect
        user selections."""
        selection = ""
        while selection is not "Q":
            selection = ""
            print("\n"*80)
            print("Game Options:\n")
            print("1 - Number of Decks: {}".format(options.number_of_decks))
            print("2 - Dealer Hits on Soft 17: {}".format("Enabled" if
                                                          options.hit_soft_17
                                                          else "Disabled"))
            print("3 - Early Surrender: {}".format("Enabled" if
                                                   options.early_surrender
                                                   else "Disabled"))
            print("4 - No Surrender: {}".format("Enabled" if
                                                options.no_surrender
                                                else "Disabled"))
            print("5 - Resplitting Allowed: {}".format("Enabled" if
                                                       options.resplitting
                                                       else "Disabled"))
            print("6 - Resplit Aces: {}".format("Enabled" if
                                                options.resplit_aces
                                                else "Disabled"))
            print("7 - Hit Split Aces: {}".format("Enabled" if
                                                  options.hit_split_aces
                                                  else "Disabled"))
            print("8 - Split By Rank/Value: {}".format("Rank" if
                                                       options.split_by_rank
                                                       else "Value"))
            print("9 - No Double After Split: ", end="")
            print("{}".format("Enabled" if options.no_double_after_split
                              else "Disabled"))
            print("10 - Double on 9-10-11 ", end="")
            print("Only: {}".format("Enabled" if options.double_9_10_11
                                    else "Disabled"))
            print("11 - Double on 9-10 Only: {}".format("Enabled" if
                                                        options.double_9_10
                                                        else "Disabled"))
            print("R - Reset to Defaults")
            print("Q - Return to Previous Screen")
            selection = input("{} ".format(choice(icons)))

            if selection.upper() == "Q":
                return options
            else:
                options = self.options_menu_input(selection, options)

    def options_menu_input(self, selection, options):
        """ This method receives a selection from the options menu
        and updates the game options object to reflect the desired
        ruleset selected by the player."""
        if selection == "1":
            try:
                decks = int(input("Choose number of decks (8 max){} ".format(
                    choice(icons))))
                if decks < 1 or decks > 8:
                    raise ValueError
                options.number_of_decks = decks
            except ValueError:
                input("Invalid input.  Press enter to continue.")
        elif selection == "2":
            options.hit_soft_17 = not options.hit_soft_17
        elif selection == "3":
            options.early_surrender = not options.early_surrender
            if options.no_surrender:
                options.no_surrender = False
        elif selection == "4":
            options.no_surrender = not options.no_surrender
            if options.early_surrender:
                options.early_surrender = False
        elif selection == "5":
            options.resplitting = not options.resplitting
        elif selection == "6":
            options.resplit_aces = not options.resplit_aces
        elif selection == "7":
            options.hit_split_aces = not options.hit_split_aces
        elif selection == "8":
            options.split_by_rank = not options.split_by_rank
        elif selection == "9":
            options.no_double_after_split = (not
                                             options.no_double_after_split)
        elif selection == "10":
            options.double_9_10_11 = not options.double_9_10_11
            if options.double_9_10:
                options.double_9_10 = False
        elif selection == "11":
            options.double_9_10 = not options.double_9_10
            if options.double_9_10_11:
                options.double_9_10_11 = False
        elif selection.upper() == "R":
            options = GameOptions()

        return options

    def load_game_menu(self, game):
        try:
            with open("saves.dat", "rb") as save_file:
                data = pickle.load(save_file)
                for player in enumerate(data):
                    print("{} - {} ${}".format(player[0]+1,
                                               player[1]["name"],
                                               player[1]["money"]))
        except FileNotFoundError:
            print("No save games found!")
            input()
            return
        while True:
            try:
                selection = int(input("Select player to load {} ".format(
                    choice(icons)))) - 1
                game.player.load_player_state(data[selection]["hash"], game)
                break
            except (ValueError, IndexError):
                print("Invalid selection.")

        return game
