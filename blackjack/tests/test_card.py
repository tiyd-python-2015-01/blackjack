from blackjack.card import Card


def test_card_class():
    card_1 = Card("10", "Spades")
    assert card_1.suit == "Spades"
    assert card_1.rank == "10"
