from blackjack.player import Player
from blackjack.carddeckshoe import Card


def test_create_player():
    player = Player()

def test_get_hand():
    player = Player()
    player.get_hand(['1','2'])
    assert player.cards == ['1','2']
    assert player.cash == 100

def test_get_card():
    player = Player()
    player.get_hand([Card("One","Diamond"),Card("Two","Hears")])
    player.get_card(Card("Three","Spades"))
    assert len(player.cards) == 3
    player.get_card(Card("Four","Spades"))
    assert len(player.cards) == 4
