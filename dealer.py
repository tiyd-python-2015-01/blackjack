"""Dealer Class"""
"""Dealer collaborates with Hand, Shoe, and Game"""
"""Dealer is responsible for having a hand with a value and taking a turn."""

from hand import Hand
from shoe import Shoe
# from player import Player
from card import Card


class Dealer():

    def __init__(self):
        self.dealer_hand = Hand()


    def __str__(self):
        return "The dealer has {}".format(self.dealer_hand)


    def dealer_turn(player_hand_value):
        while True:
            dealer_hand_value = dealer_hand.get_hand_value()
            if dealer_hand_value > 22:
                print("Dealer busts. You win!")
                player.bank += 10
                return False
            elif dealer_hand_value == 21:
                print("Dealer has Blackjack. You lose.")
                player.bank -= 10
                return False
            elif dealer_hand_value >= 17:
                print("Dealer has {}.".format(dealer_hand_value))
                if dealer_hand_value >= player_hand_value:
                    print("You lose.")
                    player.bank -= 10
                    print("You have {} dollars left in your bank.".format(player.bank))
                    return False
                else:
                    print("You win! Dealer had {}.".format(dealer_hand_value))
                    player.bank += 10
                    return False
            elif dealer_hand_value < 17:
                dealer_hand.add_card(Shoe.deal_card(Shoe()))
                print(dealer_hand)
                return dealer_hand

            else:
                print("You win! Dealer had {}.".format(dealer_hand_value))
                player.bank += 10
                return False
