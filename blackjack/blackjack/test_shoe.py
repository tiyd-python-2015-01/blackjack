from card import Card
from deck import Deck
from shoe import Shoe

def test_shoe_length():
  shoe_1_deck = Shoe(1)
  #assert len(shoe_1_deck.shuffle) == 52
  assert shoe_1_deck.decks == 1
