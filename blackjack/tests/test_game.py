from blackjack.game import Game
from blackjack.player import Player
from blackjack.carddeckshoe import Card
from blackjack.carddeckshoe import Deck
from blackjack.carddeckshoe import Shoe



def test_create_game():
    cardgame = Game()
    assert cardgame.user.cash == 100

def test_deal_cards():
    cardgame = Game()
    cardgame.shoe = Shoe()
    cardgame.deal_cards()
    assert len(cardgame.user.cards) == 2
    assert len(cardgame.dealer.cards) == 2
