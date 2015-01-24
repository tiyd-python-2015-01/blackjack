suit_sym_str = "♥♠♦♣"


def start_game():
    print(suit_sym_str * 4)
    print("Welcome to Black Jack")
    print(suit_sym_str * 4)



def ask_for_bet(players_money):
    while amount > players_money and not amount.isdigit():
        print("You have: {} dollars.".format(players_money))
        amount = input("How much would you like to bet?: ")
    return amount


def hit_or_stand():
    while choice != "H" or choice != "S" or choice != "R":
        choice = input("Would you like to [H]it or [S]tand?: ")
        choice = choice.upper()
    return choice

def show_table(player, dealer, pot):
    print(player.hand)
    print(dealer, "and one facedown card.")
    print("The pot is currently", pot)


def black_jack_text():
    print("BLACK JACK!")
