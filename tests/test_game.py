from card import Card, ranks, suits
from player import Player
from shoe import Shoe
from hand import Hand
import game

def test_player_creation():
    """Tests that Player is created with 100 in bank"""
    game.new_game()
    assert player.bank == 100


def test_player_hand_is_dealt_two_cards():
    """Test creation of player hand of two cards"""
    player1 = Player("Man")
    game.deal_player_hand()
    assert player1.player_hand_value >= 2


def test_dealer_hand_is_dealt_two_cards():
    """Tests the creation of a dealer hand with two cards"""
    dealer_hand = Hand()
    game.deal_dealer_hand()
    assert dealer.dealer_hand_value >= 2


def test_bank_decrease_when_busted():
    player = Player("man")
    player.bank = 10
    game.deal_player_hand()
    player.hit(player.player_hand)
    player.hit(player.player_hand)
    assert player.bank > 10
