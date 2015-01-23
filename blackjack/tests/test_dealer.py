from card import *
from hand import *
from player import *
from card import *
from dealer import *

mydealer = Dealer()

mycard1 = Card("A", "Diamonds")
mycard2 = Card("8", "Diamonds")
mycard3 = Card("9", "Hearts")
myhand = Hand()


def test_init():
    assert mydealer.__status__ == ''
    assert type(mydealer.__hand__) == Hand
    assert type(mydealer.__deck__) == Deck

def test_dealer_deals():
    assert type(mydealer.deal()) == Card
    assert mydealer.__deck__.get_length() == 51

def test_dealer_add_card():

    mydealer.add_card(mycard3)

def test_get_status():
    assert mydealer.get_status() == ''


def test_set_status():
    mydealer.updates_status('H')
    assert mydealer.get_status() == 'H'
    mydealer.updates_status('S')
    assert mydealer.get_status() == 'S'
