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

    def __init__(self, bet=0, chip_count=0):
        self.chip_count = chip_count
        self.bet = bet

    def bet_chips(self, bet):
        self.chip_count -= int(self.bet)
        return self.chip_count

    def user_pregame_input(self):
        user_request = input("Type 'bet' if you'd like to place a bet and"
                             " start a new hand.\n")

        if user_request in ['quit', 'help', 'chips']:
            return user_request
        elif user_request == 'bet':
            try:
                self.bet = int(input("How much would you like to wager?\n"))
                if self.bet <= self.chip_count:
                    return self.bet
                else:
                    print("You don't have that many chips!")
                    return self.user_pregame_input()
                return self.bet
            except:
                print("That is not a number.")
                return self.user_pregame_input()
        else:
            print('That is not a valid response.')
            return self.user_pregame_input()

    def user_in_game_input(self):
        user_request = input("What would you like to do? You can either:\n"
                             "Type 'hit' to receive another card.\n"
                             "Type 'stay' to hold your position.\n"
                             "Type 'double' to double down your bet\n")

        if user_request not in ['hit', 'stay', 'double',
                                'help', 'quit', 'chips']:
            print("That is not a valid response.")
            return self.user_in_game_input()
        return user_request
