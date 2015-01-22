from card import *
from hand import *
from player import *
from card import *
from dealer import *

mydealer = Dealer()

mycard1 = Card("A", "Diamonds")
mycard2 = Card("8", "Diamonds")
mycard3 = Card("9", "Hearts")
myhand = Hand(mycard1, mycard2)


def test_init():
    assert mydealer.__status__ == ''
    assert mydealer.__hand__ == []


def test_get_status():
    assert mydealer.get_status() == ''


def test_set_status():
    mydealer.updates_status('H')
    assert mydealer.get_status() == 'H'
    mydealer.updates_status('S')
    assert mydealer.get_status() == 'S'
