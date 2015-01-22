from blackjack.player_hand import Player_hand
from blackjack.dealer_hand import Dealer_hand

def test_get_hand():
    new_cards = Player_hand(["7 of Diamonds","10 of Hearts"])
    assert new_cards.cards == ["7 of Diamonds","10 of Hearts"]

def test_
