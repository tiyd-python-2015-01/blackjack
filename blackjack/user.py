import blackjack.game_file
import sys

class User:
    """User bets, hand actions, and chip count.

    Responsibilities:

    * Gives initial chip count:
        500
    * Chooses game settings:
        Change bet?
        Deal Hand

    Collaborators:

    * Chooses possible actions passed from Hand
    * Chooses how much to bet.
    * Game_manager class sends user double bet if wins. """


    def __init__(self):
        self.chip_count = 500

    def bet_chips(self, bet):
        self.chip_count = self.chip_count - bet
        return self.chip_count

    def user_pregame_input(self):
        user_request = input("How much would you like to bet? Type in"
                         " the desired amount and press enter."
                         " Type in 'deal' when you're ready for a hand")
        return user_request

    def user_pregame_steps(self, user_pregame):

        if user_request == 'help':
            blackjack.game_file.game_help()
            return user_pregame_input()

        elif user_request == 'quit':
            return sys.exit()

        elif user_request == type(int):
            bet_chips(user_request)
            print("You've bet {} chips.".format(user_request))
            return user_pregame_input()

        elif user_request == 'deal':
            return 'deal'

    def user_in_game_input(self):
        user_request = input("")

    def user_in_game_actions(self, user_wish):
        if user_request == 'help':
            print(game_help())
        elif user_request == 'quit':
            return sys.exit()
        elif user_request == 'hit':
            return 'something'
        elif user_request == 'stay':
            return 'something'
