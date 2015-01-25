from shoe import Shoe

def test_shoe_contains_decks():
    my_shoe = Shoe()
    my_shoe.total = my_shoe.set(1)
    assert len(my_shoe.total) == 52

def test_another_shoe_length():
    my_shoe = Shoe()
    my_shoe.total = my_shoe.set(3)
    assert len(my_shoe.total) == 156

def test_draw_from_total_shoe():
    my_shoe = Shoe()
    my_shoe.total = my_shoe.set(3)
    my_shoe.draw()
    assert len(my_shoe.total) == 155
