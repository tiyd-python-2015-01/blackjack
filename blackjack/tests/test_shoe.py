from blackjack.deck import Shoe

def test_shoe_class():
    new_shoe = Shoe(2)
    assert len(new_shoe) == 104
    new_card = new_shoe.deal_card()
    assert len(new_shoe) == 103
    other_shoe = Shoe(6)
    assert len(other_shoe) == 312
