"""Create classes for Blackjack"""
import random


class Hand:
    """Hand will know which cards it has, the value of those cards.
       It will receive two cards to start, then more depending on player
       action."""

    def __init__(self, Card):

        self.value = get_rank(Card)
        values = {"1" : 1, "2" : 2,"3" : 3, "4" : 4, "5" : 5, "6" : 6,
                  "7" : 7, "8" : 8, "9": 9, "10" : 10, "J" : 10, "Q" : 10,
                  "K" : 10, "A" : 1]

        hand_value = sum(self.value(Card))



class Deck:
    """The deck will collect all 52 cards. It will be able to shuffle"""
    def __init__(self, Card):

        self.ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J",
                      "Q", "K", "A"]
        self.suits = ["Hearts", "Spades", "Clubs", "Diamonds"]

        deck = [Card(name, suit) for rank in self.ranks for suit in self.suits]
        return deck
        print deck



class Card:
    """Has a rank and a suit. Aces have no value until drawn into a hand"""
    def __init__(self, suit, rank):


        self.rank = rank
        self.suit = suit

    def get_suit():
        return self.suit

    def get_rank():
        return self.rank




class Shoe:
    """Collects decks. Shuffles. Deals cards to hands"""
    def __init__(self):


    def shoe_shuffle():
            random.shuffle(self?)
