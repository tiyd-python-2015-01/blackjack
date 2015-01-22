from card import Card
from deck import Deck

def test_deck():
    a_deck = Deck()
    assert len(a_deck.cards) == 52
    assert type(a_deck.cards) == list
    
