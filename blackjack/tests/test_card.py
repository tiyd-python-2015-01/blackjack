import card

def test_card_init():
    new_card = card("Diamonds", 4)
    assert str(new_card) == "D4"
