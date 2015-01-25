from game_state import Game


def test_initial_hands():
    game = Game()
    game.deal()
    assert len(game.player_hand.cards) == 2
    assert len(game.dealer_hand.cards) == 2


def test_player_hit():
    game = Game()
    game.deal()
    game.hit()
    assert len(game.player_hand.cards) == 3


def test_dealer_hit():
    game = Game()
    game.deal()
    game.dealer_hit()
    assert len(game.dealer_hand.cards) == 3
