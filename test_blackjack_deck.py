from card import Card
from deck import Deck


def test_deck_generate():
    assert Deck()


def test_deck_str_output():
    assert Deck().__str__() == ('2♡2♢2♧2♤3♡3♢3♧3♤4♡4♢4♧4♤5♡5♢5♧5♤'
                                '6♡6♢6♧6♤7♡7♢7♧7♤8♡8♢8♧8♤9♡9♢9♧9♤'
                                '10♡10♢10♧10♤J♡J♢J♧J♤Q♡Q♢Q♧Q♤K♡K♢K♧'
                                'K♤A♡A♢A♧A♤')


def test_shuffled_deck_generate():
    assert (Deck().shuffled_deck())


def test_deck_shuffled():
    ordered_deck = Deck().__str__()
    assert (Deck().shuffled_deck()) != ordered_deck
