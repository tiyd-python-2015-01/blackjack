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


deal_player_hand()
deal_dealer_hand()

def player_turn():
    while True:
        player_hand_value = player.player_hand.get_hand_value()
        if player_hand_value < 21:
            user_turn = input("Press H to hit, or S to stand.")
            if user_turn == "h".lower():
                new_card = Shoe.deal_card(shoe)
                player.hit(player.player_hand)
                print(player.player_hand)
                # return player_hand_value
            elif user_turn == "s".lower():
                dealer_turn(player_hand_value)

            else:
                user_turn = input("Press H to hit, or S to stand.")
                # return player_hand_value
        elif player_hand_value > 21:
            print("You busted. Bet lost.")
            player.bank -= 10
            print("You have {} dollars left in your bank.".format(player.bank))
            return False
        else:
            print("You have 21. Checking dealer score...")
            return False

def dealer_turn(player_hand_value):
    while True:
        dealer_hand_value = dealer_hand.get_hand_value()
        if dealer_hand_value == 21:
            print("Dealer has Blackjack. You lose.")
            player.bank -= 10
            return False
        elif dealer_hand_value >= 17:
            print("Dealer has {}.".format(dealer_hand_value))
            if dealer_hand_value >= player_hand_value:
                print("You lose.")
                player.bank -= 10
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




player_turn()
