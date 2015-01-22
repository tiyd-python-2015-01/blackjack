from card import *
from hand import *


mycard1 = Card("A", "Diamonds")
mycard2 = Card("8", "Diamonds")
mycard3 = Card("9", "Hearts")

myhand = Hand(mycard1, mycard2)


def test_init():
    assert myhand.__cards__ == [mycard1, mycard2]
    assert len(myhand.__cards__) == 2


def test_get_status():
    assert myhand.get_hand_status() == "H"


def test_set_status():
    myhand.update_hand_status("S")
    assert myhand.get_hand_status() == "S"
    myhand.update_hand_status("H")
    assert myhand.get_hand_status() == "H"


def test_hand_get_length():
    myhand = Hand(mycard1, mycard2)
    assert len(myhand) == 2


def test_add_card():
    myhand = Hand(mycard1, mycard2)
    string = "['A of Diamonds', '8 of Diamonds', '9 of Hearts']"
    assert str(myhand.add_card(mycard3)) == string
