from card import *
from hand import *
from player import *
from card import *
from dealer import *

mydealer = Dealer()

mycard1 = Card("A", "Diamonds")
mycard2 = Card("2", "Diamonds")
mycard3 = Card("3", "Hearts")
myhand = Hand()


def test_init():
    assert mydealer.__status__ == ''
    assert type(mydealer.__hand__) == Hand
    assert type(mydealer.__deck__) == Deck


def test_dealer_deals():
    assert type(mydealer.deal()) == Card
    assert mydealer.__deck__.get_length() == 51


def test_dealer_add_card():
    assert mydealer.add_card(mycard1) == ['A of Diamonds']
    assert mydealer.add_card(mycard2) == ['A of Diamonds', '2 of Diamonds']
    assert mydealer.add_card(mycard3) == ['A of Diamonds', '8 of Diamonds',
                                          '9 of Hearts']


def test_set_and_get_status():
    mydealer.set_status('H')
    assert mydealer.get_status() == 'H'
    mydealer.set_status('B')
    assert mydealer.get_status() == 'B'


def test_get_hand():
    assert mydealer.get_hand() == ['A of Diamonds', '8 of Diamonds',
                                   '9 of Hearts']


def test_and_get_hand_status():
    mydealer.set_hand_status('S')
    assert mydealer.get_hand_status() == 'S'


def get_hand_value():
    mydealer.set_hand_status('S')
    assert mydealer.get_hand_value() == 16
    mydealer.set_hand_status('H')
    assert mydealer.get_hand_value() == 6
