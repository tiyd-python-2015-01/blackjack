import os


suit_sym_str = "♥♠♦♣"
alt_sym_str = suit_sym_str[::-1]


def border_print_top():
    """Print border to seperate text."""
    print(suit_sym_str * 10)
    print(alt_sym_str * 10)


def start_game():
    """A way to introduce the game"""
    os.system("clear")
    print(suit_sym_str * 10)
    print(alt_sym_str * 10)
    print("Welcome to Black Jack")
    print(alt_sym_str * 10)
    print(alt_sym_str * 10)


def early_surrender_text(pot):
    """Losing because of early surrender text."""
    border_print_top()
    print("You chose to surrender early, you lost ${}.".format((pot / 2)))


def ask_for_bet(players_money):
    """Prompts for the play for Bet size."""
    while True:
        print("You have: {} dollars.".format(players_money))
        amount = input("How much would you like to bet?: ")
        if amount.isdigit() and int(amount) <= players_money:
            return int(amount)
        else:
            print("That was not a number, please try again.")


def player_choice():
    """Promts the player to pick what they'd like to do in a turn."""
    choice_string = "Would you like to [H]it, [S]tand, or [D]ouble down?: "
    while True:
        choice = input(choice_string)
        choice = choice.upper()
        if choice == "H":
            return "H"
        elif choice == "S":
            return "S"
        elif choice == "D":
            return "D"
        else:
            print("You did not type H, S, or D. Please try again.")


def show_table(player, dealer, pot):
    """Displays information to the players """
    border_print_top()
    print("Your hand", player.hand)
    print("The dealer's hand", dealer.hand, "and one facedown card.")
    print("The pot is currently", pot)


def show_table_later(player, dealer, pot):
    """Displays information for the player, but with the face down card
    revealed."""
    border_print_top()
    print("Your hand", player.hand)
    print("The dealer's hand", dealer.hand)
    print("The pot is currently", pot)


def bust_lose_text(pot):
    """Text if the player goes bust."""
    border_print_top()
    print("You busted! Sorry, you lose ${}.".format(pot))


def player_win_text(pot):
    """Text for if the player wins."""
    border_print_top()
    print("You win!!!. You won, $[].".format(pot * (1.5)))


def dealer_win(dealer_hand_value, player_hand_value, pot):
    """Text for if the dealer wins."""
    border_print_top()
    print("""The dealers hand value of {}, was higher than the value of
          your hand {}. You lose ${}.""".format(dealer_hand_value,
                                                player_hand_value,
                                                pot))


def push(dealer_hand_value, player_hand_value):
    """Printed text for if there is a push."""
    border_print_top()
    print("""Your hand value {}, tied with the dealers hand value {}.
          You lose nothing.""".format(dealer_hand_value, player_hand_value))


def dealer_busts(pot):
    """Printed text for if the dealer goes bust."""
    border_print_top()
    print("The Dealer has bust, you win ${}!".format(pot))


def insurance_bet(pot):
    """Returns the amount the play wants to bet for insurance, they may only
    bet half of the original pot."""
    while True:
        insurance_limit = (pot / 2)
        print("How much would you like to bet?)
        bet = input("You can only bet up to ${}: ".format((insurance_limit)))
        if bet.isdigit() and bet <= insurance_limit:
            return int(bet)
        print("That was not a number or you bet more than you are able.")


def yes_or_no():
    while True:
        choice = input("[Y]es or [N]o?: ").upper()
        choice.upper()
        if choice == "Y":
            return True
        elif choice == "N":
            return False
        print("You did not enter Y or N, please try again.")


def play_again():
    """Gives the option for the player to play the game again."""
    border_print_top()
    print("Would you like to play again")
    return yes_or_no()


def bet_insurance_choice():
    """Returns True if the player wants to bet insurance and False if they
    do not want to bet insurance."""
    border_print_top()
    print("Would you like bet insurance")
    return yes_or_no()


def early_surrender():
    """Input for surrendering early"""
    border_print_top()
    print("Would you like to surrender")
    return yes_or_no()
