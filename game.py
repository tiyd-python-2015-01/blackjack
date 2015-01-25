from card import Card, ranks, suits
from player import Player
from shoe import Shoe
from hand import Hand

# def new_game():
player = Player(name=input("What's your name? "))
shoe = Shoe()
dealer_hand = Hand()

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


deal_player_hand()
deal_dealer_hand()

while True:
    player_hand_value = player.player_hand.get_hand_value()
    dealer_hand.get_hand_value()
    if player_hand_value < 21:
        user_turn = input("Press H to hit, or S to stand.")
        if user_turn == "h".lower():
            new_card = Shoe.deal_card(shoe)
            player.hit(player.player_hand)
            print(player.player_hand)
        elif user_turn == "s".lower():
            dealer_turn()
        else:
            user_turn = input("Press H to hit, or S to stand.")
    elif player_hand_value > 21:
        print("You busted. Bet lost.")
        player.bank -= 10
        print(player.bank)
        break
