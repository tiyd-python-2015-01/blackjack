from card import Card
from deck import Deck
from player import Player

def test_player_bank():
    player1 = Player()
    assert player1.bank == 100

def default_test_hand_value():
    player1 = Player()
    assert player1.hand_value == 0


def test_hand_value_with_cards():
    new_player = Player()
    new_player.hand = [Card("Jack", "Clubs"), Card(9, "Spades")]
    assert new_player.hand_value() == 19


def test_hand_len_with_hit():
    new_deck = Deck()
    player1 = Player()
    player1.take_a_hit(new_deck)
    player1.take_a_hit(new_deck)
    assert len(player1) == 2
