from card import Card


def test_card_string():
    new_card = Card("Diamonds", "4")
    assert str(new_card) == "D4"


def test_card_comparison():
    new_card = Card("Diamonds", "4")
    second_card = Card("Diamonds", "4")
    third_card = Card("Spades", "4")
    fourth_card = Card("Diamonds", "8")
    assert new_card == second_card
    assert not new_card == third_card
    assert not new_card == fourth_card
