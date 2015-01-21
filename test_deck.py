from deck import Deck
from card import Card

SUITS = ('Spade', 'Hearts', 'Diamonds', 'Clubs')
RANKS = (2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace')

def test_create_deck():
    deck1 = Deck()
    assert len(deck1.cards) == 52
    assert print(Card(2, "Clubs")) == print(deck1.cards[3])
