from shoe import Shoe


def test_create_shoe():
    shoe1 = Shoe(6)
    assert shoe1.number_of_decks == 6

    shoe2 = shoe1
    shoe2.shuffle()

    assert shoe1 == shoe2
