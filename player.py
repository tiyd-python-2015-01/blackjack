"""Player Class"""
"""Player collaborates with Hand"""
"""PLayer is responsible for choosing to hit, stay, quit and bet"""

from hand import Hand
from shoe import Shoe


class Player():

    def __init__(self, name):

        self.name = name
        self.bank = 100
        self.player_hand = Hand()


    def __str__(self):
        pass


    def hit(self, player_hand):
        """Player gets another card from the shoe. Hand value is recounted"""
        player_hand.add_card(Shoe.deal_card(Shoe()))
        player_hand.get_hand_value()
        return player_hand


    def stand(self):
        """Dealer will be dealt cards until game over"""
        pass

    def walk(self):
        """Player leaves game with X dollars. Must be called in-game by player"""
        user_go = input("Are you sure you want to leave?  ")
        if user_go == "y".lower():
            game_over = "Game over"
            return game_over

    def bet(self):
        self.bank -= 10
        return self.bank
