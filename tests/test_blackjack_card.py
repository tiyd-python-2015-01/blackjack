from card import Card

def test_card_is_generated():
    assert Card(rank='Q', suit='♡').__str__() == 'Q♡'


def test_identical_cards_are_equal():
    queen1 = Card('Q', 'Hearts')
    queen2 = Card('Q', 'Hearts')
    assert queen1 == queen2


def test_card_value():
    testcard = Card('2', '♡')
    assert testcard.value == 2


def test_facecard_value():
    testcard = Card('Q', '♡')
    assert testcard.value == 10


def test_ace_value():
    testcard = Card('A', '♡')
    assert testcard.value == 11
