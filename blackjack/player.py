"""
Player
    Responsibilities:
        -Name   -Hand   -Makes choices each turn?
    Collaborators
        -Game   -Hand   -Game_State

Dealer
    Responsibilities:
        -Stores Hand    -Plays by set of rules
    Collaborators
        -Hand   -Player     -Game

Human_Player
    Responsibilities:
        -Stores Hand    -Plays according to user input
    Collaborators
        -Hand   -Player     -Game

Hand
    Responsibilites:
        -Store list of cards in hand
    Collaborators
        -Player         -Card       -Game
"""


class Player:
    def __init__(self):
        self.cards = []
        self.potential_values = []
        self.cash = 100

    def get_hand(self,new_cards):
        """receives a list of Cards and stores as players cards"""
        self.cards = new_cards

    def get_card(self,new_card):
        self.cards.append(new_card)

    def display_hand(self):
        try:
            hand = ""
            for card in self.cards:
                hand += str(card)+"\n"
            return hand[0:-1]
        except:
            return "Player has an empty hand."

class Dealer(Player):
    def __init__(self):
        super().__init__()

    def display_hand(self):
        try:
            temp_cards = self.cards[1:]
            hand = ""
            for card in temp_cards:
                hand += str(card)+"\n"
            return hand[0:-1]
        except:
            return "Dealer has an empty hand."

class Hand:
    def __init__(self):
        self.cards = []
        self.potential_values = []
