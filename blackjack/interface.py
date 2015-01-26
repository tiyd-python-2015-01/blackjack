import os
import time


suit_sym_str = "♥♠♦♣"
alt_sym_str = suit_sym_str[::-1]


def border_print():
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
    border_print()
    print("You chose to surrender early, you lost ${}".format((pot / 2)))


def ask_for_bet(players_money):
    """Prompts for the play for Bet size."""
    while True:
        print("You have: ${}".format(players_money))
        amount = input("How much would you like to bet?: ")
        if amount.isdigit() and int(amount) <= players_money:
            return int(amount)
        else:
            print("That was not a proper bet. Please try again.")


def player_choice():
    """Promts the player to pick what they'd like to do in a turn."""
    border_print()
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
    """Displays information to the players."""
    border_print()
    print("Your hand", player.hand)
    print("The dealer's hand", dealer.hand, "and one facedown card.")
    print("The pot is currently ${}".format(pot))
    time.sleep(2)


def show_table_later(player, dealer, pot):
    """Displays information for the player, but with the face down card
    revealed."""
    border_print()
    print("Your hand", player.hand)
    print("The dealer's hand", dealer.hand)
    print("The pot is currently", pot)
    time.sleep(2)


def bust_lose_text(pot):
    """Text if the player goes bust."""
    border_print()
    print("You busted! Sorry, you lose ${}".format(pot))


def player_win_text(pot):
    """Text for if the player wins."""
    border_print()
    print("You win!!! You win, ${}".format(pot * (1/2)))


def player_win_jackblack(pot):
    """Text for if the player wins with blackjack."""
    border_print()
    print("You got Blackjack!!! You win, ${}".format(pot * (1/2)))


def dealer_blackjack_win(dealer_hand, player_hand, pot):
    """Text for if the dealer wins with blackjack."""
    border_print()
    print("The dealer had blackjack, you lose ${}".format(dealer_hand.value,
                                                          player_hand.value,
                                                          pot))


def dealer_win(dealer_hand, player_hand, pot):
    """Text for if the dealer wins."""
    border_print()
    print("The dealers hand value of {}, was higher than the value of"
          "your hand {}. You lose ${}.".format(dealer_hand.value,
                                               player_hand.value,
                                               pot))


def push(dealer_hand_value, player_hand_value):
    """Printed text for if there is a push."""
    border_print()
    print("Your hand value {}, tied with the dealers hand value {}."
          "You lose nothing.".format(dealer_hand_value, player_hand_value))


def dealer_busts(pot):
    """Printed text for if the dealer goes bust."""
    border_print()
    print("The Dealer has bust, you win ${}!".format(pot * (1/2)))


def insurance_bet(pot):
    """Returns the amount the play wants to bet for insurance, they may only
    bet half of the original pot."""
    while True:
        insurance_limit = (pot / 2)
        print("How much would you like to bet?")
        bet = input("You can only bet up to ${}: ".format((insurance_limit)))
        if bet.isdigit() and float(bet) <= insurance_limit:
            return int(bet)
        print("That was not a number or you bet more than you are able.")


def won_insurance_bet(side_bet):
    """Text if player wins insurance side bet."""
    border_print()
    if side_bet > 0:
        print("The dealer had blackjack, you won the insurance bet.")
        print("You win ${}.".format(side_bet))


def lost_insurance_bet(side_bet):
    """Text if player loses insurance side bet."""
    border_print()
    if side_bet > 0:
        print("The dealer did not have blackjack, you lose the insurance bet.")
        print("You lose ${}".format(side_bet))


def yes_or_no():
    """A function to take any input that only needs a yes or no."""
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
    border_print()
    print("Would you like to play again")
    return yes_or_no()


def bet_insurance_choice():
    """Returns True if the player wants to bet insurance and False if they
    do not want to bet insurance."""
    border_print()
    print("Would you like bet insurance")
    return yes_or_no()


def early_surrender():
    """Input for surrendering early"""
    border_print()
    print("Would you like to surrender")
    return yes_or_no()


def no_more_money():
    print("I'm afraid you don't have anymore money to bet.")
    print("You cannot play anymore, sorry.")
