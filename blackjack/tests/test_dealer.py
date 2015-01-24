from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.player import Player
from blackjack.dealer import Dealer

def test_shown_cards():
    dealer = Dealer()
    a_hand = Hand()
    a_hand.cards = [Card('2', 'Hearts'), Card('3', 'Diamonds')]
    test_card = dealer.shown(a_hand)
    assert test_card.rank == '3'
    assert test_card.suit == 'Diamonds'


def test_hit_test():
    dealer = Dealer()
    a_hand = Hand(value=16)
    b_hand = Hand(value=17)
    c_hand = Hand(value=18)
    a_hand.cards = [Card('7', 'Hearts'), Card('9', 'Diamonds')]
    b_hand.cards = [Card('7', 'Hearts'), Card('10', 'Diamonds')]
    c_hand.cards = [Card('8', 'Hearts'), Card('10', 'Diamonds')]

    assert dealer.hit_test(a_hand) == "HIT"
    assert dealer.hit_test(b_hand) == "STAND"
    assert dealer.hit_test(c_hand) == "STAND"

    d_hand = Hand(value=16)
    e_hand = Hand(value=17)
    f_hand = Hand(value=18)
    d_hand.cards = [Card('A', 'Hearts'), Card('5', 'Diamonds')]
    e_hand.cards = [Card('A', 'Hearts'), Card('6', 'Diamonds')]
    f_hand.cards = [Card('A', 'Hearts'), Card('7', 'Diamonds')]

    assert dealer.hit_test(d_hand) == "HIT"
    assert dealer.hit_test(e_hand) == "HIT"
    assert dealer.hit_test(f_hand) == "STAND"
