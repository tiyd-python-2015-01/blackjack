from game import *
from deck import *
from card import *
from player import *
from dealer import *
from hand import *


def is_blackjack(card1,card2):
    if card1.get_rank() == "A" and card2.get_rank() in ["10","J", "Q", "K"]:
        return True
    elif card2.get_rank() == "A" and card1.get_rank() in ["10","J", "Q", "K"]:
        return True
    else:
        return False

def initialize_player(mydealer,myplayer,p_card1,p_card2):
#Initial dealing of 2 cards to player
    myplayer.add_card(p_card1)
    myplayer.add_card(p_card2)
    myplayer.set_hand_status("H")
    print ("Your first card is {}".format(p_card1))
    print ("Your second card is {}".format(p_card2))
    if p_card1.get_rank() == "A":
        num = int(input ("Do you want that A to count as 1 or 11? "))
        if num == 11:
            myplayer.set_hand_status("S")
    elif p_card2.get_rank() == "A":
         num = int(input ("Do you want that A to count as 1 or 11? "))
         if num == 11:
             myplayer.set_hand_status("S")
    else:
        print("player hand value",myplayer.get_hand_value())

def initialize_dealer(mydealer,d_card1,d_card2):
    #Initial 2 cards to dealer
    mydealer.add_card(d_card1)
    mydealer.add_card(d_card2)
    mydealer.set_hand_status("H")
    if d_card1.get_rank() == "A" or d_card2.get_rank() == "A":
        if d_card1.get_value() + d_card2.get_value() + 10 <= 21:
                mydealer.set_hand_status("S")
    print ("dealer {}".format(d_card1))
    print ("dealer {}".format(d_card2))
    print ("dealer hand value",mydealer.get_hand_value())


def dealer_plays(mydealer):
    mydealer.updates_status('H')
    while mydealer.get_hand_value() < 17:
        print("My current hand is: {}".format(mydealer.get_hand()))
        d_card = mydealer.deal()
        mydealer.set_hand_status("H")
        print ("My new card is {}".format(d_card))

        if d_card.get_rank() == "A":
            if mydealer.get_hand_status() == "S":
                mydealer.set_status("H")
            else:
                if mydealer.get_hand_value() + d_card.get_value() + 10 <= 21:
                    mydealer.set_hand_status("S")
                elif mydealer.get_hand_value() + d_card.get_value() > 21:
                    mydealer.updates_status("B")
        else:
            if mydealer.get_hand_value() + d_card.get_value() > 21:
                if mydealer.get_hand_status() == "S":
                    if mydealer.get_hand_value() + d_card.get_value() - 10 <= 21:
                        mydealer.set_hand_status("H")
                    else:
                       mydealer.updates_status("B")
                else:
                    mydealer.updates_status("B")

        mydealer.add_card(d_card)

def player_plays(myplayer,mydealer):
    myplayer.updates_status("H")
    while myplayer.get_status() == "H":
        print("Your current hand is: {}".format(myplayer.get_hand()))
        myplayer.updates_status(input("Hit (H) or Stand? (S) "))
        if myplayer.get_status() != "S":
            p_card = mydealer.deal()
            print ("Your card is {}".format(p_card))

            if p_card.get_rank() == "A":
                if myplayer.get_hand_status() == "S":
                    myplayer.set_status("H")
                else:
                    if myplayer.get_hand_value() + p_card.get_value() + 10 <= 21:
                        myplayer.set_hand_status("S")
                    elif myplayer.get_hand_value() + p_card.get_value() > 21:
                        myplayer.updates_status("B")
            else:
                if myplayer.get_hand_value() + p_card.get_value() > 21:
                    if myplayer.get_hand_status() == "S":
                        if myplayer.get_hand_value() + p_card.get_value() - 10 <= 21:
                            myplayer.set_hand_status("H")
                        else:
                           myplayer.updates_status("B")
                    else:
                        myplayer.updates_status("B")

            myplayer.add_card(p_card)

def play_game():
    print("Lets play Blackjack")
    print("-------------------")
# Creates a game
    blackjack = {'dealer': False, "player": False}
    mygame = Game()
    name = input("What is your name dear victim? I mean Player? ")
    budget = 100
    bet=10
    myplayer = Player(name,budget)
    mydealer = Dealer()
# Deals initial 2 cards to the player- checks for blackjack
    p_card1, p_card2 = mydealer.deal(), mydealer.deal()
    if not is_blackjack(p_card1,p_card2):
        initialize_player(mydealer,myplayer,p_card1,p_card2)
# Deals initial 2 cards - checks for blackjack
    else:
        print("blackjack player")
        blackjack['player'] = True
    print("-------------------------")
    print ("I will now get my 2 cards!")
    d_card1, d_card2 = mydealer.deal(), mydealer.deal()
    if not is_blackjack(d_card1,d_card2):
        initialize_dealer(mydealer,d_card1,d_card2)
    else:
        print("blackjack dealer")
        blackjack['dealer'] = True

# if they both have blackjacks game ends
    if (blackjack['dealer'] == True and
        blackjack['player'] == True):
        mygame.set_winner("T")
        print ("We both had a blackjack.  It is a Push")
    else:
        if blackjack['player'] == True:
            mygame.set_winner("P")
            print ("Player wins with a Black Jack")
        elif blackjack['dealer'] == True:
            mygame.set_winner("D")
            print ("Dealer wins with a Black Jack")
        else:  # There were no blackajcks
            player_plays(myplayer,mydealer)
            if myplayer.get_status() == "S":
                print ("now to the dealer")
                dealer_plays(mydealer)
                if mydealer.get_status() == "B":
                    print ("the dealer has busted")
                    mygame.set_winner("P")
                else:
                    if mydealer.get_hand_value() > myplayer.get_hand_value():
                        mygame.set_winner("D")
                    elif mydealer.get_hand_value() < myplayer.get_hand_value():
                        mygame.set_winner("P")
                    else:
                        mygame.set_winner("T")
            else:
                print("Busted!! You lose my friend")
                mygame.set_winner("D")
    #if mygame.get_winners()
    print(mygame.get_winners())

play_game()
