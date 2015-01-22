import game_state as gs


def test_create_game_state():
    state = gs.Game_State()
    assert state.cards == []
