from card import Card

def test_card_init():
    new_card = Card("Diamonds", 4)
    assert str(new_card) == "D4"
