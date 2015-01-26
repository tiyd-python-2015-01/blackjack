from game import *
from deck import *
from card import *
from player import *
from dealer import *
from hand import *
import os

# Checks to see if the 2 initial cards are blackjack
# (value of 21 points with 2 cards)


def is_blackjack(card1, card2):
    if card1.get_rank() == "A" and card2.get_rank() in ["10", "J", "Q", "K"]:
        return True
    elif card2.get_rank() == "A" and card1.get_rank() in ["10", "J", "Q", "K"]:
        return True
    else:
        return False

# validate card adds a card to a hand after doing all
# the checks to handle the Aces and the special situations they have
# When there is already an Ace with a value of 11 (Soft hand)
# and that value of 11 needs to be changed to 1 (turning the hand into Hard)
# it handles all special cases for the Ace in the hand


def validate_card(player, card):
    if card.get_rank() == "A":
        if player.get_hand_status() == "S":
            player.set_status("H")
        else:
            if player.get_hand_value() + card.get_value() + 10 <= 21:
                player.set_hand_status("S")
            elif player.get_hand_value() + card.get_value() > 21:
                player.set_status("B")
    else:
        if player.get_hand_value() + card.get_value() > 21:
            if player.get_hand_status() == "S":
                if player.get_hand_value() + card.get_value() - 10 <= 21:
                    player.set_hand_status("H")
                else:
                    player.set_status("B")
            else:
                player.set_status("B")

    player.add_card(card)
    return player

# initialize adds the first 2 cards to player and dealer hands
# if possible to add a A with a value of 11, it does so by setting
# the hand to Soft. If not, the hand is Hard and the Ace will have
# a value of 1


def initialize(player, card1, card2):
    # Initial 2 cards to dealer
    player.add_card(card1)
    player.add_card(card2)
    player.set_hand_status("H")
    if card1.get_rank() == "A" or card2.get_rank() == "A":
        if card1.get_value() + card2.get_value() + 10 <= 21:
                player.set_hand_status("S")
    return player

# dealer_plays manages a loop for the dealer dealing a new card,
# adding it to the hand, as long as the value of the hand is
# smaller than 17


def dealer_plays(mydealer):
    mydealer.set_status('H')
    print("Finally my turn!!!")
    print('Here I go')
    while mydealer.get_hand_value() < 17:
        print("My current hand is: {}".format(mydealer.get_hand()))
        d_card = mydealer.deal()
        mydealer.set_hand_status("H")
        print("My new card is {}".format(d_card))
        mydealer = validate_card(mydealer, d_card)

# player_plays manages a loop for the player dealing a new card
# adding it to the hand, and asking the use if they want to hit or stand


def player_plays(myplayer, mydealer):
    myplayer.set_status('H')
    while myplayer.get_status() == "H":
        print("Your current hand is: {}".format(myplayer.get_hand()))
        while True:
            action = input("Hit (H) or Stand? (S) ").upper()
            if action in ["H", "S"]:
                break
        myplayer.set_status(action)
        if myplayer.get_status() != "S":
            p_card = mydealer.deal()
            print("Your card is {}".format(p_card))
            myplayer = validate_card(myplayer, p_card)
            if myplayer.get_hand_value() == 21:
                myplayer.set_status('S')

# print status lets the player knows how many games they have won, lost or tied


def print_status(game):
    print('--------------')
    print("GLOBAL SCORES")
    print('You have won {} games'.format(game.get_winners().count("P")))
    print('I have won {} games'.format(game.get_winners().count("D")))
    print('And we have Tied {} times'.format(game.get_winners().count("T")))
    print('--------------')

# main program loop.


def play_game():
    os.system('clear')
    print("Lets play Blackjack")
    print("-------------------")
# Creates a game
    mygame = Game()
    budget = 100
    bet = 10
    name = input("What is your name dear victim? I mean Player? ")
    play = True
    print('-------------------------------------------------')
    print("Let's Play.  Your initial budget for betting is: {}".format(budget))
    print('-------------------------------------------------')
    while play and budget > 0:
        myplayer = Player(name, budget)
        mydealer = Dealer()
        blackjack = {'dealer': False, "player": False}
# Deals initial 2 cards to the player- checks for blackjack
        p_card1, p_card2 = mydealer.deal(), mydealer.deal()
        print("{}, Your first card is {}".format(myplayer.get_name(), p_card1))
        print("and your second card is {}".format(p_card2))
        if not is_blackjack(p_card1, p_card2):
            myplayer = initialize(myplayer, p_card1, p_card2)
        else:
            blackjack['player'] = True
            myplayer.add_card(p_card1)
            myplayer.add_card(p_card2)
# Deals initial 2 cards to dealer - checks for blackjack
        print("-------------------------")
        print("DEALER: I will now get my 2 cards!")
        d_card1, d_card2 = mydealer.deal(), mydealer.deal()
        print("One of my cards is: {}".format(d_card1))
        print("The other card is hidden")
        print()
        if not is_blackjack(d_card1, d_card2):
            mydealer = initialize(mydealer, d_card1, d_card2)
        else:
            blackjack['dealer'] = True
            mydealer.add_card(d_card1)
            mydealer.add_card(d_card2)

# if they both have blackjacks game ends in tie
        if (blackjack['dealer'] and blackjack['player']):
            mygame.set_winner("T")
            print("We both had a blackjack.  It is a Push")
        else:
            # if player has a blackjack, player wins 1.5 the bet
            if blackjack['player']:
                mygame.set_winner("P")
                myplayer.set_budget(bet*1.5)
                print("{}\r".format(myplayer.get_name()))
                print(" You win with a BlackJack")
            elif blackjack['dealer']:
                mygame.set_winner("D")
                myplayer.set_budget(-bet)
                print("Dealer wins with a Black Jack")
            else:  # There were no blackjacks
                # player now gets the chance to get additional cards or Stand
                player_plays(myplayer, mydealer)
                if myplayer.get_status() == "S":
                    # if player did not bust, it is the dealer's turn
                    os.system('clear')
                    dealer_plays(mydealer)
                    if mydealer.get_status() == "B":
                        print("You win. The dealer has busted")
                        mygame.set_winner("P")
                        myplayer.set_budget(bet)
                    else:
                        if (mydealer.get_hand_value() >
                           myplayer.get_hand_value()):
                            mygame.set_winner("D")
                            print("And I win!!")
                            myplayer.set_budget(-bet)
                        elif (mydealer.get_hand_value() <
                              myplayer.get_hand_value()):
                            mygame.set_winner("P")
                            print("You win\r",)
                            print("".format(myplayer.get_name()))
                            myplayer.set_budget(+bet)
                        else:
                            mygame.set_winner("T")
                            print("It is a tie")
                else:
                    print("Busted!! You lose my friend")
                    mygame.set_winner("D")
                    myplayer.set_budget(-bet)
        print('---------------------------------------------')
        print("The dealer\'s hand was {}".format(mydealer.get_hand()))
        print("Your hand was {}".format(myplayer.get_hand()))
        print_status(mygame)
        budget = myplayer.get_budget()
        print("You have ${}".format(budget))
        while True:
            play_again = input("Do you want to play again? Y/N. ").upper()
            if play_again in ["Y", "N"]:
                break
        if play_again == "N":
            play = False
        os.system('clear')

if __name__ == '__main__':
    play_game()
