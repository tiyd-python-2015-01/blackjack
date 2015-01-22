from card import Card
from deck import Deck
from player import Player

def test_Card():

    new_card = Card("King", "Spade")
    assert new_card.number == "King"
    assert new_card.suit == "Spade"



def test_deck():

    new_deck = Deck()
    assert len(new_deck) == 52
    new_deck.get_card()
    assert len(new_deck) == 51
    assert isinstance(new_deck.get_card(), Card)
    assert isinstance(new_deck.deck[1], Card)

def test_player():

    new_deck = Deck()
    new_player = Player(100,new_deck)
    new_player.get_hand()
    assert len(new_player) == 2
    assert len(new_deck) == 50
    new_player.hit()
    assert len(new_deck) == 49
    assert len(new_player) == 3
    assert new_player.pot == 100
    new_player.bet()
    assert new_player.pot == 90
    new_player.bet()
    assert new_player.bet
