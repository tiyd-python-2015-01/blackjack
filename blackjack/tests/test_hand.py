from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.hand import Hand

def test_get_card():
    a_deck = Deck()
    a_hand = Hand()
    a_hand.get_card(a_deck)
    assert len(a_hand.cards) == 1
    assert len(a_deck.cards) == 51

def test_valuation():
    a_hand = Hand()
    a_hand.cards =[Card('2', 'Hearts'), Card('10', 'Spades')]
    assert a_hand.valuation() == 12
    
