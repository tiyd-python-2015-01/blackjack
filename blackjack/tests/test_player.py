from player import Player


def test_player_creation():
    player = Player("Alan")
    assert player


def test_player_attributes():
    player = Player("Alan")
    assert player.name == "Alan"
    assert player.money == 100
    assert player.hands == []


def test_modify_money():
    player = Player("Alan")
    player.modify_money(100)
    assert player.money == 200
    player.modify_money(-50)
    assert player.money == (150)


def test_modify_money_exception():
    player = Player("Alan")
    try:
        player.modify_money(-101)
    except ValueError:
        assert True
