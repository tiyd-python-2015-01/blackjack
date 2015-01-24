from card import Card, ranks, suits
from shoe import Shoe
from hand import Hand
from player import Player


def test_deck_creation_in_shoe_class():
    """Tests the ability of the shoe to create deck"""
    test_deck = Shoe()
    assert len(test_deck.deck) == 52


def test_shuffle():
    """test the ability of the shoe to shuffle a deck"""
    deck1 = Shoe()
    deck2 = Shoe()
    deck1.shuffle_shoe()
    deck2.shuffle_shoe()
    assert deck1.shuffle_shoe() != deck2.shuffle_shoe()


def test_for_dealing_card():
    """Will test that the shoe has dealt a card. Length of shoe should be 51"""
    deck1 = Shoe()
    deck1.deal_card()
    assert len(deck1.deck) == 51
