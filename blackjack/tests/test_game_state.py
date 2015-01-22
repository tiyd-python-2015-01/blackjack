import game_state as gs


def test_create_Table_State():
    state = gs.Table_State()
    assert state.cards == []
