from player import Player


def test_player_creation():
    player = Player("Alan")
    assert player


def test_player_attributes():
    player = Player("Alan")
    assert player.name == "Alan"
    assert player.money == 1000
    assert player.hands == []


def test_modify_money():
    player = Player("Alan")
    player.modify_money(1000)
    assert player.money == 2000
    player.modify_money(-500)
    assert player.money == (1500)


def test_modify_money_exception():
    player = Player("Alan")
    try:
        player.modify_money(-1001)
    except ValueError:
        assert True
