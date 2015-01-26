from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.hand import Hand


def test_get_card():
    a_deck = Deck()
    a_hand = Hand()
    a_hand.get_card(a_deck)
    assert len(a_hand.cards) == 1
    assert len(a_deck.cards) == 51


def test_new_card():
    a_hand = Hand()
    a_hand.cards = [Card('2', 'Hearts'), Card('10', 'Spades')]
    test_card = a_hand.new_card()
    assert test_card.rank == '10'
    assert test_card.suit == 'Spades'


def test_valuation_non_ace():
    a_hand = Hand()
    a_hand.cards = [Card('2', 'Hearts'), Card('10', 'Spades')]
    assert a_hand.valuation() == 12


def test_valuation_ace_test():
    a_hand = Hand()
    b_hand = Hand()
    c_hand = Hand()
    d_hand = Hand()
    a_hand.cards = [Card('A', 'Hearts'),
                    Card('5', 'Spades'),
                    Card('K', 'Clubs')]
    b_hand.cards = [Card('A', 'Hearts'),
                    Card('A', 'Spades'),
                    Card('K', 'Clubs')]
    c_hand.cards = [Card('A', 'Hearts'),
                    Card('A', 'Spades')]
    d_hand.cards = [Card('A', 'Hearts'),
                    Card('5', 'Spades')]

    assert a_hand.valuation() == 16
    assert b_hand.valuation() == 12
    assert c_hand.valuation() == 12
    assert d_hand.valuation() == 16
