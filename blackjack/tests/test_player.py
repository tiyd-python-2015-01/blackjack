from card import *
from hand import *
from player import *
from card import *

myplayer = Player("Ana", 100)

mycard1 = Card("A", "Diamonds")
mycard2 = Card("8", "Diamonds")
mycard3 = Card("9", "Hearts")
myhand = Hand()
myhand.add_card(mycard1)
myhand.add_card(mycard2)


def test_init():
    assert myplayer.__name__ == "Ana"
    assert myplayer.__budget__ == 100


def test_get_budget():
    assert myplayer.get_budget() == 100


def test_set_budget():
    myplayer.set_budget(10)
    assert myplayer.get_budget() == 110
    myplayer.set_budget(-10)
    assert myplayer.get_budget() == 100


def test_get_and_set_status():
    myplayer.set_status('S')
    assert myplayer.get_status() == 'S'


def test_dealer_add_card():
    assert myplayer.add_card(mycard1) == ['A of Diamonds']
    assert myplayer.add_card(mycard2) == ['A of Diamonds', '2 of Diamonds']
    assert myplayer.add_card(mycard3) == ['A of Diamonds', '8 of Diamonds',
                                          '9 of Hearts']


def test_get_hand():
    assert myplayer.get_hand() == ['A of Diamonds', '8 of Diamonds',
                                   '9 of Hearts']


def test_and_get_hand_status():
    myplayer.set_hand_status('S')
    assert myplayer.get_hand_status() == 'S'


def get_hand_value():
    myplayer.set_hand_status('S')
    assert myplayer.get_hand_value() == 16
    myplayer.set_hand_status('H')
    assert myplayer.get_hand_value() == 6
