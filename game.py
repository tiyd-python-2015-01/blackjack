from card import Card, ranks, suits
from player import Player
from shoe import Shoe
from hand import Hand

# def new_game():
shoe = Shoe()
dealer_hand = Hand()
player = Player("John")


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


# def player_turn():
#     while True:
#         player_hand_value = player.player_hand.get_hand_value()
#         check_has_ace()
#         if player_hand_value < 21:
#             user_turn = input("Press H to hit, or S to stand.")
#
#             if user_turn == "h".lower():
#                 new_card = Shoe.deal_card(shoe)
#                 player.hit(player.player_hand)
#                 print(player.player_hand)
#             elif user_turn == "s".lower():
#                 player.stand()
#             elif user_turn == "q".lower():
#                 player.walk()
#             else:
#                 user_turn = input("Press H to hit, or S to stand.")
#
#         elif player_hand_value > 21:
#             print("You busted. Bet lost.")
#             player.bank -= 10
#             print("You have {} dollars left in your bank.".format(player.bank))
#             return False
#
#         else:
#             print("You have 21. Checking dealer score...")
#             return False



def check_has_ace():
    has_ace = False
    if "A" in player.player_hand.hand and player_hand_value == 11:
        player_hand_value += 10
        return True
    else:
        return


deal_player_hand()
deal_dealer_hand()
player_turn()
