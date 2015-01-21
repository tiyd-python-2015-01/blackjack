import Deck as dk
import Card
import Shoe

def test_deck_creation():
    test_deck = dk.Deck()
    assert len(test_deck.deck) == 52
    assert isinstance(test_deck.deck[0], Card.Card)

def test_card_creation():
    test_card = Card.Card
    assert str(Card.Card("Jack", "Diamonds")) == "Jack of Diamonds"

def test_shuffle():
    test_deck = Shoe.Shoe()
    assert len(test_deck.shuffle_shoe) == 52
