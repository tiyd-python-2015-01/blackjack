Alan Grissett
alan.grissett@gmail.com

The Iron Yard - Durham
Python Development - Cohort 3
[ Key:
       + - Implemented
       * - Not Yet Implemented
       ? - Unsure if should be included in class
       \ - Planned But Low Priority
]
Blackjack Project

The goal of this project is to complete a fully functional console based
version of Blackjack.  The game will allow the player to select options for
the rules used in the play of the game - including the number of decks used,
dealer hit/stand on soft 17, early/late surrender, hit/resplit aces,
insurance, double on 9/10/11 or 10/11 only and no double on split.

The game will be divided into classes for each component of the game.
The initial class plan is as follows and is subject to change:


+ <Card>: The Card class will contain the information about a single card in the
deck.  Cards will have attributes for rank, suit and value.  Numbered cards
are worth their face value, while Jacks, Queens and Kings are worth 10.  Aces
are worth 1 or 11 depending on the player's current hand value.  The Card
class will provide a method for updating the value of the ace if requested
to do so by the game.

The Card objects will be created and stored by the Deck class and will
subsequently be distributed to Hand objects assigned to the player and
dealer respectively.

To Do:
+ - Assign class attributes
+ - Add method to evaluate the value of Card
+ - Add ASCII representations of suits
+ - Add method for swapping value of Aces


+ <Deck>: The Deck class will be an object containing a collection of at least
one full deck of cards upon initialization.  The Deck will construct a list
containing at least one of each card in a standard playing deck and then
use a random number generator to randomize the location of the cards within
the list.  The Deck defaults to having a single set of 52 cards, but has an
optional argument to contain any number of decks (with a maximum of 8).
The Deck contains methods to reshuffle the deck and to remove cards from
the list and return their values to the requester.

To Do:
+ - Generate a list containing Card objects representing a full deck of cards
+ - Randomize card locations within the deck list
+ - Add optional class attribute to increase the number of decks of Card
    objects created
+ - Add a method to remove a card from the card list and return the value
+ - Add a method to reshuffle the deck of cards


+/ <Player>:  The player class object will contain the amount of money the
player has remaining to wager and a list of hands (multiple hands on split)
controlled by the player.

To Do:
+ - Add class attributes
+ - Add methods to increment or decrement remaining money
+ - Add name attribute
/ - Add method to save player state so the game can be resumed with current
    money amount maintained


* <Dealer>: The Dealer class will contain a single Hand object corresponding
to the cards it is dealt.  It will also contain a rule set for deciding
whether to hit or stand for it's given hand value.

To Do:
+ - Add class attribute
+ - Add basic decision rules
/ - Add optional rules based on user selected options


+ <Hand>:  The Hand class will contain a list of cards currently associated
with a Player or Dealer.  It will have a method for determining and returning
the current value of itself and a method to receive new cards from the deck
and add them to the class's Card list.

To Do:
+ - Add class attribute and initialization
+ - Add method to evaluate value of cards
+ - Add method to request change in the value of an ace if present in the hand
+ - Add method to receive Card objects and add them to the Hand's Card list


* <GameOptions>:  The GameOptions class will store all of the user selected
rules for gameplay.  Attributes will include an integer value between 1 and
8 representing the number of decks to be used in the game, as well as a
series of Boolean values with default values that will activate or deactivate
certain rule variations.

To Do:
+ - Add basic list of class attributes, starting with number of decks
+ - Add in common rule variations.  No hit on soft 17 and Late/Early surrender
+ - Add in advanced rule variations


* <Game>:  The Game class will be the backbone of the game.  It will store
the wager amount made by the player, created and distribute Hand objects to
the Player and Dealer and will control game flow based on hand
values held by the player and dealer.  It will have methods to calculate
payouts based off of results of the game.  Payouts will be 2:1 for a standard
win and 3:2 on blackjack.  The Game class will pass the payout information
for use by the Player class to update the Player's money total.  ?May create
the Dealer object and retrieve the ruleset from GameOptions.?

To Do:
* - Add list of Game attributes
* - Add method to distribute Hands to Player and Dealer
* - Add method to check the status of the game by resolving Hand values
* - Add method to distribute payouts to the player
? - Add method for determining available actions for the player (Maybe in Hand
    Class?)
? - Add method to retrieve the ruleset from GameOptions and create the
    Dealer based on currently selected rules. (Maybe in Blackjack class?)


* <Run>:  The Blackjack class will be the driver script for the game.
It will control all of the program flow and interact with the Game and
Interface Classes to start new hands, request menu displays, request output
to the console from the Interface Class.  This file will contain the
main method for the game, and will be the script executed to start the
game.

To Do:
* - Plan overall program flow and determine best structure for this class
* - Add main method to initialize the game and start program flow


* <Interface>:  The Interface class will contain all of the ASCII text that
will be used for in-game card representations, menus and methods for
receiving input from the user.

To Do:
+ - Design main menu
* - Design options menu
* - Add method for updating options based on user input from options menu
* - Add method for displaying current hands for the dealer and player to
    the console
* - Add method to display win/lose text after each hand
...more


/////<PyGameInterface>:  Very unlikely, but this class would replace the
Interface class to provide a graphical game experience.  The interface
would allow for mouse input or keyboard input corresponding to available
menu options or avaiable actions within the game.  The rest of the
functionality would be identical to interface.

To Do:
* - The rest of the project
