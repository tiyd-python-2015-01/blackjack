from blackjack.carddeckshoe import Card
from blackjack.carddeckshoe import Deck
from blackjack.carddeckshoe import Shoe


def test_create_card():
    card1 = Card(10, "Club")
    card2 = Card("King", "Diamond")
    assert card1.face == 10
    assert card1.suit == "Club"
    assert card2.face == "King"
    assert card2.suit == "Diamond"


def test_create_deck():
    """Test if 52 Cards are created"""
    deck = Deck()
    assert len(deck.cards) == 52
    assert isinstance(deck.cards[0], Card)


def test_get_card():
    deck = Deck()
    assert isinstance(deck.get_card(), Card)
    assert len(deck.cards) == 51
    assert isinstance(deck.get_card(), Card)
    assert len(deck.cards) == 50


def test_create_shoe():
    shoe = Shoe()
    assert len(shoe.decks) == 1
    shoe = Shoe(3)
    assert len(shoe.cards) == 156
    assert isinstance(shoe.cards[0], Card)


def test_shuffle_shoe():
    shoe = Shoe()
    card = shoe.cards[0]
    shoe.shuffle_shoe()
    assert shoe.cards[0] != card
    assert shoe.cards.index(card) >= 0
