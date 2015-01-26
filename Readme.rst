Jason Aylward
Homework 6 - Blackjack Game


To run:

At the terminal:
>> python blackjack

The game will ask you if you would like to quit at the end of every round.
If you would like to end the game sooner, simply enter 'quit'





The Blackjack Game is divided into quite a number of classes. Most perform
fairly unique operations but a few share enough similarity that I am not sure
if they will make it to the final stage.

From the top down, I image the game's loop to be managed by the class Game.
Game will loop between the user interface, the game state and
the player's states (dealer and player).  It will also manage the communication
between these three large entities.

Game_State simply holds what cards are on the table and manages the shoe of
cards.  It will need to give cards to the Game class when requested from the
players.

The Player class will have two subclasses, Dealer and Human_Player (hopefully
renamed soon).  Each holds a hand (or more) of cards.  The Dealer will have
some rules to control its behavior.  The HumanPlayer's behavior will be
dictated by the user via the Interface class.

The other classes are all card related.
A Card is simply a face (1-10, J,Q,K,A) and its suit.
A Deck is all 52 unique cards
A Shoe is 1 or more Decks

A Hand is a little more interesting.  A Hand will contain 3 or more Cards but
will also contain a valuation method that uses the cards on the Table plus the
cards stored in the hand.  This valuation method will compute multiple values
depending on the Ace's duality and return the best value for each situation.

Players (HumanPlayer or Dealer) will forfeit if their hand busts and will return
a Win if hitting 21.  The Game class will receive these events and relay them to
the user through the Interface.
