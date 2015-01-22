from card import Card
"""Test functions for the card class"""


def test_card_attributes():
    new_card_A = Card("A", "clubs")
    new_card_2 = Card("2", "hearts")
    new_card_3 = Card("3", "spades")
    new_card_4 = Card("4", "diamonds")
    new_card_5 = Card("5", "clubs")
    new_card_6 = Card("6", "hearts")
    new_card_7 = Card("7", "spades")
    new_card_8 = Card("8", "diamonds")
    new_card_9 = Card("9", "clubs")
    new_card_10 = Card("10", "hearts")
    new_card_J = Card("J", "spades")
    new_card_Q = Card("Q", "diamonds")
    new_card_K = Card("K", "clubs")

    assert new_card_A.rank == "A"
    assert new_card_2.rank == "2"
    assert new_card_3.rank == "3"
    assert new_card_4.rank == "4"
    assert new_card_5.rank == "5"
    assert new_card_6.rank == "6"
    assert new_card_7.rank == "7"
    assert new_card_8.rank == "8"
    assert new_card_9.rank == "9"
    assert new_card_10.rank == "10"
    assert new_card_J.rank == "J"
    assert new_card_Q.rank == "Q"
    assert new_card_K.rank == "K"

    assert new_card_A.suit == "clubs"
    assert new_card_2.suit == "hearts"
    assert new_card_3.suit == "spades"
    assert new_card_4.suit == "diamonds"
    assert new_card_5.suit == "clubs"
    assert new_card_6.suit == "hearts"
    assert new_card_7.suit == "spades"
    assert new_card_8.suit == "diamonds"
    assert new_card_9.suit == "clubs"
    assert new_card_10.suit == "hearts"
    assert new_card_J.suit == "spades"
    assert new_card_Q.suit == "diamonds"
    assert new_card_K.suit == "clubs"

    assert new_card_A.value == 11
    assert new_card_2.value == 2
    assert new_card_3.value == 3
    assert new_card_4.value == 4
    assert new_card_5.value == 5
    assert new_card_6.value == 6
    assert new_card_7.value == 7
    assert new_card_8.value == 8
    assert new_card_9.value == 9
    assert new_card_10.value == 10
    assert new_card_J.value == 10
    assert new_card_Q.value == 10
    assert new_card_K.value == 10


def test_swap_ace():
    new_card = Card("A", "hearts")
    assert new_card.value == 11
    new_card.swap_ace()
    assert new_card.value == 1
