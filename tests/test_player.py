from card import Card, ranks, suits
from shoe import Shoe
from hand import Hand
from player import Player


def test_hit():
    """tests the ability of the player to add a card to his/her hand"""
    shoe = Shoe()
    hand = Hand()
    test_player = Player("Dean")
    print(hand)
    print(test_player.hit(hand))
    assert hand.get_hand_value() >= 2


# def test_walk():
#     """Tests ability for player to quit game. Must be called in-game"""
#     test_player = Player("Dean")
#     assert test_player.walk == "Game over"

def test_player_bet():
    test_player = Player("Dean")
    test_player.bet()
    assert test_player.bank == 90

    
