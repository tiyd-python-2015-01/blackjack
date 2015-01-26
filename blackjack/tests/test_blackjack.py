from card import *
from blackjack import *


mycard = Card("J", "Diamonds")
mycard1 = Card("A", "Diamonds")
mycard2 = Card("3", "Diamonds")
myplayer = Player("ana", 100)


def test_is_blackjack():
    assert is_blackjack(mycard, mycard1)
    assert is_blackjack(mycard1, mycard)
    assert is_blackjack(mycard, mycard2) is False
    assert is_blackjack(mycard1, mycard2) is False
    assert is_blackjack(mycard1, mycard1) is False


def test_initialize():
    myplayer = Player("ana", 100)
    myplayer = initialize(myplayer, mycard, mycard1)
    assert myplayer.get_hand_value() == 21
    myplayer = Player("ana", 100)
    initialize(myplayer, mycard1, mycard2)
    assert myplayer.get_hand_value() == 14


def test_validate_card():
    myplayer = Player("ana", 100)
    myplayer.add_card(mycard1)
    myplayer.set_hand_status("S")
    validate_card(myplayer, mycard2)
    assert myplayer.get_hand_value() == 14
    myplayer.set_hand_status("H")
    validate_card(myplayer, mycard)
    assert myplayer.get_hand_value() == 14

    myplayer = Player("ana", 100)
    myplayer.add_card(mycard)
    myplayer.set_hand_status("H")
    myplayer = validate_card(myplayer, mycard2)
    assert myplayer.get_hand_value() == 13
    myplayer = validate_card(myplayer, mycard1)
    assert myplayer.get_hand_value() == 14
