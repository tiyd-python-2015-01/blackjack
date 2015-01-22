from card import *

mycard = Card("J", "Diamonds")
mycard1 = Card("A", "Diamonds")
mycard2 = Card("8", "Diamonds")


def test_init():
    assert mycard.rank == "J"
    assert mycard.suit == "Diamonds"


def test_getvalue():
    assert mycard.get_value() == (10)
    assert mycard1.get_value() == (1, 11)
    assert mycard2.get_value() == (8)
