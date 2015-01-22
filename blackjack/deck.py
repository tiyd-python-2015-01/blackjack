class Deck:
    """A deck is a collection of cards, typically containing one of
    each rank/suit combination.

    Responsibilities:
    A deck must shuffle, producing a random ordering of its constituent cards.
    A deck must pop off cards, removing them from the deck and delivering them
    to some other object (likely a hand, but potentially a discard pile).

    Collaborators:
    A deck will be reconstituted and shuffled by the game before each round of
    play.
    A deck holds cards.
    A deck sends cards to various hands. 
    """
