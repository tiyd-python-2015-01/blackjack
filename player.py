"""Player Class"""
"""Player collaborates with Hand"""
"""PLayer is responsible for choosing to hit, stay, quit and bet"""

from hand import Hand


class Player():

    def __init__(self, name):

        self.name = name
        self.bank = 100


    def __str__(self):
        pass


    def hit(self):
        Hand.add_card
        Hand.get_hand_value
