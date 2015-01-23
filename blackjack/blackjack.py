from game import *
from deck import *
from card import *
from player import *
from dealer import *
from hand import *

def is_it_blackjack(card1,card2):
    if card1.get_rank() == "A" and card2.get_rank() in ["10","J", "Q", "K"]:
        return True
    elif card2.get_rank() == "A" and card1.get_rank() in ["10","J", "Q", "K"]:
        return True
    else:
        return False

def initialize_dealer(mydealer):
    hand_type = "H"
    #Game follows with dealer dealing 2 cards to dealer
    print ("I will now get my 2 cards!")
    d_card1, d_card2 = mydealer.deal(), mydealer.deal()
    print ("dealer", is_it_blackjack(d_card1,d_card2))
    if not is_it_blackjack(d_card1,d_card2):
        if d_card1.get_rank() == "A" and d_card2.get_rank() == "A":
           hand_type = "S"
           mydealer.add_card(d_card1,"S")
           mydealer.add_card(d_card2,"S")

        elif d_card1.get_rank() == "A" or d_card2.get_rank() == "A":
           if d_card1.get_value() + d_card2.get_value() + 10 <= 21:
               mydealer.add_card(d_card1,"S")
               mydealer.add_card(d_card2,"S")
           else:
                mydealer.add_card(d_card1,"H")
                mydealer.add_card(d_card2,"H")
        else:
            mydealer.add_card(d_card1,"H")
            mydealer.add_card(d_card2,"H")
    else:
        hand_type = "S"
        mydealer.add_card(d_card1,hand_type)
        mydealer.add_card(p_card2,hand_type)
        print ("wow dealer blackjack")

    print ("dealer {}".format(d_card1))
    print ("dealer {}".format(d_card2))

    print (mydealer.__deck__.get_length())
    print ("dealer hand value",mydealer.get_hand_value())

def initialize_player(mydealer,myplayer):
    hand_type = "H"
#Game start with dealer dealing 2 cards to player
    p_card1, p_card2 = mydealer.deal(), mydealer.deal()
    print ("Your first card is {}".format(p_card1))
    print ("Your second card is {}".format(p_card2))
    print ("player", is_it_blackjack(p_card1,p_card2))
    if not is_it_blackjack(p_card1,p_card2):
        if p_card1.get_rank() == "A" and p_card2.get_rank() == "A":
            hand_type = "S"
            myplayer.add_card(p_card1,"S")
            myplayer.add_card(p_card2,"S")

        elif p_card1.get_rank() == "A" or p_card2.get_rank() == "A":
            num = int(input ("Do you want that A to count as 1 or 11? "))
            if num == 11:
                hand_type = "S"
            myplayer.add_card(p_card1,hand_type)
            myplayer.add_card(p_card2,hand_type)
        else:
            hand_type="H"
            myplayer.add_card(p_card1,hand_type)
            myplayer.add_card(p_card2,hand_type)
    else:
        hand_type = "S"
        myplayer.add_card(p_card1,"S")
        myplayer.add_card(p_card2,"S")
        print ("wow! blackjack")

    print (mydealer.__deck__.get_length())
    print ("player hand value",myplayer.get_hand_value())


def play_game():
    print("Lets play Blackjack")
    print("-------------------")
# Creates a game
    mygame = Game()

    name = input("What is your name dear victim? I mean Player? ")
    budget = 100
    bet=10
    myplayer = Player(name,budget)
    mydealer = Dealer()
# Creates a player and deals initial 2 cards
    initialize_player(mydealer,myplayer)

# Creates a dealer

    initialize_dealer(mydealer)



play_game()
