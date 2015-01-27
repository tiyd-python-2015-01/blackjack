from blackjack.deck import Deck
from blackjack.player import Player


def test_player_class():
    new_player = Player()
    assert len(new_player.hand) == 0
    new_deck = Deck()
    new_player.take_card(new_deck)
    assert len(new_deck) == 51
    assert len(new_player.hand) == 1


def test_player_making_bet():
    new_player = Player()
    new_player.pay_out(10)
    assert new_player.money == 90
    new_player.pay_out(80)
    assert new_player.money == 10


def test_player_winning():
    new_player = Player()
    pot = 20
    new_player.get_money(pot)
    assert new_player.money == 120
