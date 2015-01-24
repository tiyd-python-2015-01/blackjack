from dealer import Dealer
from player import Player
from game import Game
from hand import Hand
from card import Card
from deck import Deck, Clubs, Diamonds, Hearts, Spades

def test_new_turn():
    dealer = Dealer()
    player = Player("John")
    deck = Deck()
    game = Game(dealer, player, deck)
    game.new_turn()
    assert game.pot == 0
    assert len(deck) == 52
    assert player.stack == 100
    assert len(player.hand.hand) == 2
    assert len(dealer.hand.hand) == 2


def test_place_bet():
    dealer = Dealer()
    player = Player("John")
    deck = Deck()
    game = Game(dealer, player, deck)
    game.new_turn()
    game.place_bet(5)
    assert player.stack == 95
    assert game.pot == 5
