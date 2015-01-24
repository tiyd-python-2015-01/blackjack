from card import Card

def test_card_rank():
    new_card = Card("King", "Clubs")
    assert new_card.rank == "King"


def test_card_suit():
    new_card = Card("King", "Clubs")
    new_card_2 = Card(9, "Spades")
    assert new_card.suit == "Clubs"
    assert new_card_2.suit == "Spades"


def test_card_value():
    new_card = Card("King", "Clubs")
    new_card_2 = Card(9, "Spades")
    new_card_3 = Card("Ace", "Diamonds")
    assert new_card.value == 10
    assert new_card_2.value == 9
    assert new_card_3.value == 11
