# Blackjack

* [Part 1](README_1.md)

#The blackjack game will consist of one game loop and several classes.
class Card will hold a suit and a number(rank), the module will also store a
list of every suit and rank. Additionaly it will have a method that can
calculate value if called.

class Deck will generate and store 52 cards in a list
(by collaborating with the card class). It will also "draw" (pop) a card from
the deck by selecting a random card from the card list.

class Player will request cards from the Deck, store a hand, and store an
amount of money that is available to bet.

Similarly, class Dealer will, take cards from Deck hold a hand and make
descisions based on values of wether to hit or stay.

Finally, Pot will keep track of bets made and pay out or take money with the
player.

The rest of the program will be implemeted in a game loop.


* [Part 2](README_2.md)

How to run the game:
  1. In terminal make the current directory the blackjack folder.
  2. Type python game_loop.py.
