from blackjack.carddeckshoe import Card
from blackjack.carddeckshoe import Deck
from blackjack.carddeckshoe import Shoe


def test_create_card():
    card1 = Card(10, "♧")
    card2 = Card("King", "♢")
    assert card1.rank == 10
    assert card1.suit == "♧"
    assert card2.rank == "King"
    assert card2.suit == "♢"

def test_card_equality():
    card1 = Card("King", "♧")
    card2 = Card("King", "♧")
    assert card1 == card2


def test_create_deck():
    """Test if 52 Cards are created"""
    deck = Deck()
    assert len(deck.cards) == 52
    assert isinstance(deck.cards[0], Card)


def test_give_card_from_deck():
    deck = Deck()
    assert isinstance(deck.give_card(), Card)
    assert len(deck.cards) == 51
    assert isinstance(deck.give_card(), Card)
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
    shoe.shuffle()
    assert shoe.cards[0] != card
    assert shoe.cards.index(card) >= 0

def test_deal_hand():
    shoe = Shoe()
    hand = shoe.deal_hand()
    assert len(hand) == 2
    assert len(shoe.cards) == 50

def test_give_card_from_shoe():
    shoe = Shoe()
    assert len(shoe.cards) == 52
    shoe.give_card()
    assert len(shoe.cards) == 51
