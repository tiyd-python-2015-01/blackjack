from card import *
from hand import *
from player import *
from card import *
from game import *


mygame = Game()


def test_init():
    assert mygame.winners == []


def test_set_winner():
    mygame.set_winner("D")
    assert mygame.winners == ["D"]
    mygame.set_winner("P")
    assert mygame.winners == ["D", "P"]


def test_get_winner():
    mygame.set_winner("T")
    assert mygame.get_winners() == ["D", "P", "T"]
