from blackjack.player import Player


def test_create_player():
    player = Player("Batman")
    assert player.name == "Batman"
