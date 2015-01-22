from card import Card

def test_card_is_generated():
    assert Card(rank='Q', suit='♡').__str__() == 'Q♡'
