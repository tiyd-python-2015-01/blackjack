from card import Card

def test_card():
    a_card = Card(2, "Spades")
    assert a_card.rank == 2
    assert a_card.suit == "Spades"

def test_card2():
    a_card = Card("Jack", "Hearts")
    assert a_card.rank == "Jack"
    assert a_card.suit == "Hearts"
