from blackjack.game import Game
from blackjack.game_state import Game_State


def test_create_game_state():
    state = Game_State()
    assert state.cards_on_table == []
    assert len(state.shoe.cards) == 52
