from card import Card
def test_Card():
    new_card = Card("King","Spade", 10)
    assert new_card.value == 10
    assert new_card.number == "King"
    assert new_card.suit == "Spade"
