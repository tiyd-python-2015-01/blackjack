from random import shuffle
from card import Card
from deck import Deck

def test_create_object():
    new_deck = Deck()
    assert type(new_deck) == Deck

def test_first_card():
    new_deck = Deck()
    assert new_deck.deck[0] == "2 of Hearts"

def test_length():
    new_deck = Deck()
    assert (len(new_deck.deck)) == 52

def test_shuttle():
    new_deck = Deck()
    assert shuffle(new_deck.deck)[0] == "Jack of Clubs"
