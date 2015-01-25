# Blackjack

* [Part 1](README_1.md)
The game layout uses 5 classes: Card, Deck, Player, Hand, and Game State
The Game State class will collect the deck(s) of cards and deal them as well
as implement the turn flow of the game and win/loss conditions. This is subject
to change as I code it out, possibly breaking up Game State into a couple more
classes for Shoe, Deal, Bet.
* [Part 2](README_2.md)
The layout now uses 6 classes and an interface (play_blackjack.py).
The game_state file sets up a new shoe and hands as well as the deal method.
The interface contains functions for intro display, hand display, the dealer's
logic, player's moves, and the evaluation and results for a round.
