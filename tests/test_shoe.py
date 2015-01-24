from shoe import Shoe


def test_create_shoe():
    shoe1 = Shoe(6)
    assert len(shoe1._cards) == 312

def test_shuffle():
    shoe1 = Shoe(6)
    shoe1.shuffle()

    assert shoe1._cards[32] != Shoe(6)._cards[32] and shoe1._cards[46] != Shoe(6)._cards[46]

def test_new_shoe_can_draw_card():
    shoe = Shoe(6)
    card = shoe.draw()

    assert len(shoe._cards) == 311
    assert card is not None
