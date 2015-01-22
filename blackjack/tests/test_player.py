import player as plyr


def test_create_player():
    player = plyr.Player("Batman")
    assert player.name == "Batman"
