from player import Player
from shoe import Shoe

def test_player_has_starting_bank():
    assert Player().bank == 100


def test_bet_loss_to_bank():
    player = Player()
    bet = 50
    player.bet(bet)
    assert player.bank == 50


def test_win_no_blackjack():
    player = Player()
    bet = 100
    player.bet(bet)
    player.win_no_blackjack(bet)
    assert player.bank == 200


def test_win_with_blackjack():
    player = Player()
    bet = 100
    player.bet(bet)
    player.win_blackjack(bet)
    assert player.bank == 250
