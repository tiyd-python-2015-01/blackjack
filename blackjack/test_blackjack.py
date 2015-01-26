from cards import Card
from deck import Deck

def test_deck_len():
    new_deck = Deck()
    assert (len(new_deck.deck)) == 52

def test_create_card():
    new_card = Card("King", "Clubs")
    assert type(new_card) == Card

def test_card_value():
    new_card = Card("Ace", "Clubs")
    new_card2 = Card(9, "Spades")
    new_card3 = Card("Queen", "Hearts")
    assert new_card.value == 11
    assert new_card2.value == 9
    assert new_card3.value == 10

def test_rank():
    new_card = Card("Ace", "Clubs")
    new_card2 = Card(9, "Spades")
    new_card3 = Card("Queen", "Hearts")
    assert new_card.rank == "Ace"
    assert new_card2.rank == 9
    assert new_card3.rank == "Queen"

def test_suit():
    new_card = Card("Ace", "Clubs")
    new_card2 = Card(9, "Spades")
    new_card3 = Card("Queen", "Hearts")
    assert new_card.suit == "Clubs"
    assert new_card2.suit == "Spades"
    assert new_card3.suit == "Hearts"
