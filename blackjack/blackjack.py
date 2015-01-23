from game import *
from deck import *
from card import *
from player import *
from dealer import *
from hand import *


def play_game():
    print("Lets play Blackjack")
    print("-------------------")
# Creates a game
    mygame = Game()
# Creates a dealer
    mydealer = Dealer()
# Creates a player
    budget = 100
    bet=10
    name = input("What is your name dear victim? I mean Player? ")
    myplayer = Player(name,budget)
#Game start with dealer dealing 2 cards to player
    p_card1, p_card2 = mydealer.deal(), mydealer.deal()
    myplayer.add_card(p_card1)
    myplayer.add_card(p_card2)
    print ("Dear {}, your first card is {}".format(name, p_card1))
    print ("Dear {}, your second card is {}".format(name, p_card2))
    print (mydealer.__deck__.get_length())
    #Game follows with dealer dealing 2 cards to dealer
    print ("Dear {}. I will now get my 2 cards!".format(name))
    d_card1, d_card2 = mydealer.deal(), mydealer.deal()
    mydealer.add_card(d_card1)
    mydealer.add_card(d_card2)
    print (mydealer.__deck__.get_length())

play_game()
