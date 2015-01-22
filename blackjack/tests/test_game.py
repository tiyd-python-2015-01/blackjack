import game,player,carddeckshoe

def test_create_game():
    cardgame = game.Game()
    assert isinstance(cardgame.user,player.Player)
    assert isinstance(cardgame.shoe,carddeckshoe.Shoe)
