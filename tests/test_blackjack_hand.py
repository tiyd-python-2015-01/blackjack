from card import Card
from deck import Deck
from hand import Hand


def test_hand_has_card():
    dummyhand = Hand()
    dummyhand.cards = [Card('2', '♡')]
    assert Card('2', '♡') in dummyhand.cards


def test_hand_value_1_card():
    dummyhand = Hand()
    dummyhand.cards = [Card('2', '♡')]
    assert dummyhand.get_value() == 2


def test_hand_value_2_cards():
    dummyhand = Hand()
    dummyhand.cards = [Card('2', '♡'), Card('4', '♡')]
    assert dummyhand.get_value() == 6


def test_hand_value_2_face_cards():
    dummyhand = Hand()
    dummyhand.cards = [Card('K', '♡'), Card('Q', '♡')]
    assert dummyhand.get_value() == 20


def test_hand_busted():
    dummyhand = Hand()
    dummyhand.cards = [Card('K', '♡'), Card('K', '♡'), Card('K', '♡')]
    assert dummyhand.get_value() == 30


def test_hand_value_win():
    dummyhand = Hand()
    dummyhand.cards = [Card('K', '♡'), Card('4', '♡'), Card('7', '♡')]
    assert dummyhand.get_value() == 21


def test_hand_value_blackjack():
    dummyhand = Hand()
    dummyhand.cards = [Card('A', '♡'), Card('Q', '♡')]
    assert dummyhand.get_value() == 'BLACKJACK'


def test_more_than_one_ace():
    dummyhand = Hand()
    dummyhand.cards = [Card('A', '♡'), Card('A', '♡')]
    assert dummyhand.get_value() == 12
