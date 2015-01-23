from card import *
from hand import *
from player import *
from card import *

mygame = Game()

def test_init():
    assert mygame.winner == ""

def test_set_winner():
    mygame.set_winner("D")
    assert mygame.winner == "D"

def test_get_winner():
    assert mygame.get_winner() == "D"
