"""Player Class"""
"""Player collaborates with Hand"""
"""PLayer is responsible for choosing to hit, stay, quit and bet"""

from hand import Hand
from shoe import Shoe
from dealer import Dealer


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
        Dealer.dealer_turn(self.player_hand_value)
        return dealer_hand


    def walk(self):
        """Player leaves game with X dollars. Must be called in-game by player"""
        user_go = input("Are you sure you want to leave?  ")
        if user_go == "y".lower():
            game_over = "Game over"
            return game_over

    def player_turn():
        while True:
            player_hand_value = player.player_hand.get_hand_value()
            check_has_ace()
            if player_hand_value < 21:
                user_turn = input("Press H to hit, or S to stand.")

                if user_turn == "h".lower():
                    new_card = Shoe.deal_card(shoe)
                    player.hit(player.player_hand)
                    print(player.player_hand)
                elif user_turn == "s".lower():
                    player.stand()
                elif user_turn == "q".lower():
                    player.walk()
                else:
                    user_turn = input("Press H to hit, or S to stand.")

            elif player_hand_value > 21:
                print("You busted. Bet lost.")
                player.bank -= 10
                print("You have {} dollars left in your bank.".format(player.bank))
                return False

            else:
                print("You have 21. Checking dealer score...")
                return False        
