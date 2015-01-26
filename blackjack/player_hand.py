from card import Card
from deck import Deck
from random import shuffle


class Player_Hand:
    """Creates a player hand.

    Responsiblities:
    * Creates a player hand by drawing card from the deck.
    * Determine the value of given cards in hand.

    Collaborators:
    * Deck
    """

    def __init__(self, hand=None):
        if hand is None:
            hand = []
        self.hand = hand
        self.money = 100

    def __str__(self):
        """Player hand is represented by string of cards"""
        return str([hand for hand in self.hand])

    def hand_size(self):
        return len(self.hand)

    def draw_two(self, deck):
        self.hand = []
        card1 = deck.draw()
        card2 = deck.draw()
        self.hand.append(card1)
        self.hand.append(card2)
        return self.hand

    def player_bet(self, money):
        if int(money) < 10:
            print("You must bet a min of 10")

        elif int(money) <= self.money and money > 10:
            self.money = self.money - money
        else:
            print("You dont have enough money")

    def hit(self, card):
        return self.hand.append(card)

    def hand_value(self):
        value = 0
        for card in self.hand:
            value = value + card.value
        return value

    def show_player_hand(self):
        """Reveals the hand to self"""
        print(self.hand)
        return self.hand
from card import Card
from deck import Deck
from random import shuffle


class Player_Hand:
    """Creates a player hand.

    Responsiblities:
    * Creates a player hand by drawing card from the deck.
    * Determine the value of given cards in hand.

    Collaborators:
    * Deck
    """

    def __init__(self, hand=None):
        if hand is None:
            hand = []
        self.hand = hand
        self.money = 100

    def __str__(self):
        """Player hand is represented by string of cards"""
        return str([hand for hand in self.hand])

    def draw_two(self, deck):
        self.hand = []
        card1 = deck.draw()
        card2 = deck.draw()
        self.hand.append(card1)
        self.hand.append(card2)
        return self.hand

    def player_bet(self, money):
        if int(money) < 10:
            print("You must bet a min of 10")

        elif int(money) <= self.money and money > 10:
            self.money = self.money - money
        else:
            print("You dont have enough money")

    def hit(self, card):
        return self.hand.append(card)

    def hand_value(self):
        value = 0
        for card in self.hand:
            value = value + card.value
        return value

    def show_player_hand(self):
        """Reveals the hand to self"""
        print(self.hand)
        return self.hand
