from blackjack.card import Card


first_card = Card("Diamonds", "4")
second_card = Card("Diamonds", "4")
third_card = Card("Spades", "4")
fourth_card = Card("Diamonds", "8")


def test_card_string():
    assert str(first_card) == "D4"


def test_card_comparison():
    assert first_card == second_card
    assert not first_card == third_card
    assert not first_card == fourth_card


def test_rank_comparison():
    assert first_card.same_rank(second_card)
