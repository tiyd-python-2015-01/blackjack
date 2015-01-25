from card import Card
from deck import Deck
from player import Player
from player import Dealer
from pot import Pot



def get_bet():
    """Takes input from the player to place in the make_bet fn"""
    try:
        return int(input("How much would you like to bet?"))
    except(ValueError):
        return get_bet()


def bet_logic(pot):
    """Makes sure bets aren't too large or small"""
    while True:
        pot.make_bet(get_bet())
        bet = pot.bet

        if bet > pot.purse:
            print("That bet is too high, please bet again.")

        elif bet < 0:
            print("Please enter only positive numbers")

        else:
            break

def player_choice(player):
    """Takes player input on whether they would like to  hit or stay, and calls
    hit function if they hit"""

    move = input("What would you like to do? [H]it or [S]tay").upper()
    if move not in "HS":
        print("Please enter H or S")
        return player_choice(player)

    if move == "H":
        player.hit()
        print("You now have: \n")
        player.view_cards()

        if player.get_value() < 21:
            player_choice(player)
    else:
        player.view_cards()

def win_game(pot):
    """Gives player their bet back and prints a win statement"""
    print("You Win!")
    pot.return_bet()
    print("Your pot is now {}".format(pot.purse))

def lose_game(pot):
    """Prints a lose statement, and players pot."""
    print("You Lose!!!")
    pot.subtract_bet()
    print("Your pot is now {}".format(pot.purse))

def game_logic(dealer,player,pot):
    """Compares values of player and dealer, and determines winner"""
    if dealer.get_value() < 17:
        dealer.hit()
        print("The dealer hits")

    print("Dealer has {}".format(dealer.get_value()))
    print("You have {}".format(player.get_value()))

    if player.get_value() > 21:
        lose_game(pot)
    elif dealer.get_value() > 21:
        win_game(pot)

    elif abs(player.get_value()-21) < abs(dealer.get_value()-21):
        win_game(pot)

    elif abs(player.get_value()-21) > abs(dealer.get_value()-21):
        lose_game(pot)


    else:
        print("Tie!")






if __name__ == '__main__':

    counter = 1
    pot = Pot(100)

    print("Welcome to Blackjack! \n")
    while True:

        new_deck = Deck()
        player = Player(new_deck)
        dealer = Dealer(new_deck)
        bet_logic(pot)

        dealer.get_hand()
        player.get_hand()
        print("Round {} \n".format(counter))
        print("Your hand: \n")
        player.view_cards()
        print("Dealer's hand: \n")
        dealer.view_cards()

        player_choice(player)

        game_logic(dealer,player,pot)

        counter += 1

        if pot.purse <= 0:
            print("You're out of money. Game over.")
            play_again = input("Would you like to play again? [Y]es, or [N]o").upper()

            if play_again == "Y":
                counter = 0
                pot = Pot(100)
                continue
            else:
                break
