from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.player import Player
from blackjack.dealer import Dealer
from blackjack.game import Game

def test_bust_check():
    game = Game()
    a_hand = Hand(value=20)
    b_hand = Hand(value=21)
    c_hand = Hand(value=22)

    assert game.bust_check(a_hand) == 'ok'
    assert game.bust_check(b_hand) == 'ok'
    assert game.bust_check(c_hand) == 'bust'


def test_higher_hand():
    game = Game()

    p_hand = Hand(value=20)
    d_hand = Hand(value=20)
    assert game.higher_hand(p_hand, d_hand) == 'push'

    p_hand = Hand(value=20)
    d_hand = Hand(value=19)
    assert game.higher_hand(p_hand, d_hand) == 'p_hand'

    p_hand = Hand(value=19)
    d_hand = Hand(value=20)
    assert game.higher_hand(p_hand, d_hand) == 'd_hand'
