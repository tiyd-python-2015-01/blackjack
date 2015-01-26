from card import Card
from hand import Hand
from shoe import Shoe, Clubs, Diamonds, Spades


def test_can_hold_cards():
    new_hand = Hand([Card(2, Diamonds), Card('A', Spades)])
    assert new_hand.hand[0] == Card(2, Diamonds)
    assert new_hand.hand[1] == Card('A', Spades)


def test_can_print_hand():
    new_hand = Hand([Card(2, Diamonds), Card('A', Spades)])
    assert repr(new_hand) == "2" + Diamonds + ", " + "A" + Spades


def test_draw_card():
    new_hand = Hand([Card(2, Diamonds), Card('A', Spades)])
    shoe = Shoe(6)
    new_hand.draw(shoe)
    assert len(new_hand.hand) == 3


def test_has_hard_total():
    new_hand1 = Hand([Card(2, Diamonds), Card('A', Spades)])
    new_hand2 = Hand([Card(4, Clubs), Card(5, Spades)])
    new_hand3 = Hand([Card(2, Diamonds), Card('K', Spades)])
    assert new_hand1.hard_total == 13
    assert new_hand2.hard_total == 9
    assert new_hand3.hard_total == 12


def test_has_soft_total():
    new_hand1 = Hand([Card(2, Diamonds), Card('A', Spades)])
    new_hand2 = Hand([Card(4, Clubs), Card(5, Spades)])
    new_hand3 = Hand([Card(2, Diamonds), Card('K', Spades)])
    new_hand4 = Hand([Card('A', Diamonds), Card('A', Spades)])
    assert new_hand1.soft_total == 3
    assert new_hand2.soft_total == 9
    assert new_hand3.soft_total == 12
    assert new_hand4.soft_total == 2


def test_bust():
    new_hand1 = Hand([Card(2, Diamonds),
                      Card('K', Spades), Card('Q', Diamonds)])
    new_hand2 = Hand([Card(4, Clubs), Card(5, Spades)])
    new_hand3 = Hand([Card(2, Diamonds), Card('K', Spades)])
    assert new_hand1.bust() is True
    assert new_hand2.bust() is False
    assert new_hand3.bust() is False


def test_can_add_cards_from_shoe():
    shoe1 = Shoe(6)
    new_hand1 = Hand([Card(2, Diamonds), Card('A', Spades)])
    new_hand1.draw(shoe1)
    assert len(new_hand1.hand) == 3
    assert len(shoe1) == 311


def test_new_hand():
    shoe1 = Shoe(6)
    new_hand1 = Hand([])
    new_hand1.new_hand(shoe1)
    assert len(new_hand1.hand) == 2


def test_reset_hand():
    new_hand1 = Hand([Card(2, Diamonds),
                      Card('K', Spades), Card('Q', Diamonds)])
    new_hand1.reset_hand()
    assert new_hand1.hand == []
    assert len(new_hand1.hand) == 0


def test_best_hand():
    new_hand = Hand([Card(9, Diamonds), Card('A', Spades), Card(9, Spades)])
    assert new_hand.best_hand == 19
    new_hand2 = Hand([Card(9, Diamonds), Card('A', Spades), Card(2, Spades)])
    assert new_hand2.best_hand == 12
