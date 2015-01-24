from game_options import GameOptions
from random import choice

icons = ["♡", "♧", "♢", "♤"]
class Interface:
    """ Interface class will provide all of the methods of interacting with
    the user.  It will contain all of the methods for displaying to the
    console as well as receiving and checking input from the player.

    Responsibilities:
    * Outputting game information and menus to the player
    * Receiving input from the player
    """

    def display_game_status(self, game):
        pass
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
        print("♡ 1 - Play Blackjack!")
        print("♧ 2 - Set Game Options")
        print("♢ 3 - Quit")
        print("-----------------------")
        selection = input("{} ".format(choice(icons)))

        return selection

    def get_bet(self, player):
        """Prompts the user to select a bet amount in multiples of 5, not
        exceeding 20"""
        print("\n"*80)
        while True:
            print("How much would you like to wager on the next hand? ")
            print("Please wager in multiples of 5.  Maximum bet is 20.")
            try:
                print("You currently have {} dollars.".format(player.money))
                bet = int(input("{} ".format(choice(icons))))
                if bet % 5 is not 0 or 0 > bet > 20:
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
            print("Q - Return to Main Menu")
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
