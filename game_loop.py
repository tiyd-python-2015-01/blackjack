from card import Card
from deck import Deck
from player import Player
from player import Dealer





while True:
    counter = 1
    new_deck = Deck()
    player = Player(100,new_deck)
    dealer = Dealer(100,new_deck)
    dealer.get_hand()
    player.get_hand()
    print("Round {}".format(counter))
    print("Your hand: \n")
    player.view_cards()
    print("Dealer's hand: \n")
    dealer.view_cards()
    move = input("What would you like to do? [H]it or [S]tay").upper()
    if move == "H":
        player.hit()
        print("You now have: \n")
        player.view_cards()

    if dealer.get_value() < 17:
        dealer.hit()
        print("The dealer hits")

    print("Dealer has {}".format(dealer.get_value()))
    print("You have {}".format(player.get_value()))

    if abs(player.get_value()-21) < abs(dealer.get_value()-21):
        print("You Win!")
        player.pot +=10
        print("Your pot is now {}".format(player.pot))

    elif abs(player.get_value()-21) > abs(dealer.get_value()-21):
        print("You Lose")
        player.pot -=10
        print("Your pot is now {}".format(player.pot))

    else:
        print("Tie!")

    play_again = input("Would you like to play again? [Y]es, or [N]o").upper()

    if play_again == "Y":
        continue
    else:
        break
