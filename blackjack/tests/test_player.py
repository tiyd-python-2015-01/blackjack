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
    myplayer.updates_budget(10)
    assert myplayer.get_budget() == 110
    myplayer.updates_budget(-10)
    assert myplayer.get_budget() == 100

def test_get_status():
    assert myplayer.get_status() == ''


def test_set_status():
    myplayer.updates_status('H')
    assert myplayer.get_status() == 'H'
    myplayer.updates_status('S')
    assert myplayer.get_status() == 'S'
