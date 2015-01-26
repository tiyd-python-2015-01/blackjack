from card import Card, ranks, suits
from player import Player
from shoe import Shoe
from hand import Hand
from dealer import Dealer

class BlackjackGame():

    def __init__():

        shoe = Shoe()
        dealer_hand = Hand()
        player = Player()


    def deal_player_hand():
        card_one = Shoe.deal_card(shoe)
        card_two = Shoe.deal_card(shoe)
        player.player_hand.add_card(card_one)
        player.player_hand.add_card(card_two)
        print(player.player_hand)
        return player.player_hand


    def deal_dealer_hand():
        card_one = Shoe.deal_card(shoe)
        card_two = Shoe.deal_card(shoe)
        dealer_hand.add_card(card_one)
        dealer_hand.add_card(card_two)
        return dealer_hand


    def game_start():
        deal_player_hand()
        deal_dealer_hand()
        player.player_turn()


def check_has_ace():
    has_ace = False
    if "A" in player.player_hand.hand and player_hand_value == 11:
        player_hand_value += 10
        return True
    else:
        return


if __name__=="__main__":
    new_game = BlackjackGame
    new_game.game_start()
