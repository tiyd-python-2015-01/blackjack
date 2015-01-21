import Deck as dk
import Card

def test_deck_creation():
    test_deck = dk.Deck()
    assert len(test_deck.deck) == 52
    assert isinstance(test_deck.deck[0], Card.Card)
