from blackjack.game import Game
from blackjack.player import Player
from blackjack.carddeckshoe import Card
from blackjack.carddeckshoe import Deck
from blackjack.carddeckshoe import Shoe
from blackjack.game_state import Game_State


def test_create_game():
    cardgame = Game()
    assert isinstance(cardgame.user, Player)
    assert isinstance(cardgame.gamestate, Game_State)
