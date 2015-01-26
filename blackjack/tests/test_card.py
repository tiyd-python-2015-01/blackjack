from card import *

mycard = Card("J", "Diamonds")
mycard1 = Card("A", "Clubs")
mycard2 = Card("8", "Hearts")


def test_init():
    assert mycard.rank == "J"
    assert mycard.suit == "Diamonds"


def test_getvalue():
    assert mycard.get_value() == 10
    assert mycard1.get_value() == 1
    assert mycard2.get_value() == 8


def test_get_rank():
    assert mycard.get_rank() == "J"
    assert mycard1.get_rank() == "A"
    assert mycard2.get_rank() == "8"


def test_get_suit():
    assert mycard.get_suit() == "Diamonds"
    assert mycard1.get_suit() == "Clubs"
    assert mycard2.get_suit() == "Hearts"
