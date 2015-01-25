from player import Player
from player import Dealer
from deck import Deck
from card import Card

new_deck = Deck()
new_player = Player(new_deck)

def test_setup_player():
    """Testing setting up a player"""
    assert len(new_player.hand) == 0

def test_get_hand():
    """Testing getting a hand and __len__ fn"""

    new_player.get_hand()

    assert len(new_player) == 2
    assert len(new_deck) == 50

def test_hit():
    """Testing whether hit takes one card from a deck and gives to player"""

    new_player.hit()
    assert len(new_deck) == 49
    assert len(new_player) == 3


def test_get_value():
    """Test adding basic card values."""
    new_player.hand = [Card("2","Diamonds"),Card("2","Hearts"),
                       Card("10","Clubs")]
    assert new_player.get_value() == 14

def test_get_value_aces():
    """Test logic for adding aces value."""
    new_player.hand = [Card("Ace","Clubs"),Card("Ace","Clubs"),Card("Ace","Clubs")]
    assert new_player.get_value() ==13
    new_player.hand = [Card("Ace","Clubs"),Card("Ace","Clubs")]
    assert new_player.get_value() == 12
    new_player.hand = [Card("Ace","Clubs"),Card("Ace","Clubs"),
                       Card("9", "Hearts")]
    assert new_player.get_value() == 21
    new_player.hand = [Card("Ace","Clubs"),Card("10","Clubs")]
    assert new_player.get_value() == 21
    new_player.hand = [Card("5","Clubs"),Card("5","Clubs"),
                       Card("Ace", "Clubs")]
    assert new_player.get_value() == 21


def test_dealer():
    """Test if sub class dealer works the same as player"""
    new_deck = Deck()
    dealer = Dealer(new_deck)
    dealer.get_hand()
    assert len(new_deck) == 50
    assert len(dealer) == 2
    dealer.hit()
    assert len(dealer) == 3
    dealer.hand = [Card("Ace","Clubs"),Card("Ace","Clubs"),Card("Ace","Clubs")]
    assert dealer.get_value() ==13
