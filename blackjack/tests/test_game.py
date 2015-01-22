from game_options import GameOptions
from game import Game
from hand import Hand


def test_create_hands():
    options = GameOptions()
    new_game = Game(options, "Alan")
    new_game.create_hands()

    assert len(new_game.player.hands[0].cards) == 2
    assert len(new_game.dealer.hand.cards) == 2
    assert len(new_game.deck.cards) == 48
