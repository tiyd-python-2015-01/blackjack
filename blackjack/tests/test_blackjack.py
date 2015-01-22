from card import Card
from deck import Deck
from player import Player
from shoe import Shoe

new_deck = Deck()
new_card = new_deck.deal_card()


def test_card_class():
    card_1 = Card("10", "Spades")
    assert card_1.suit == "Spades"
    assert card_1.rank == "10"
    card_2 = Card("King", "Diamonds")
    assert card_2.suit == "Diamonds"
    assert card_2.rank == "King"
    card_3 = Card("2", "Clubs")
    assert card_3.suit == "Clubs"
    assert card_3.rank == "2"
    assert isinstance(card_3, Card) == True


def test_deck_class():
    new_deck = Deck()
    assert len(new_deck.cards) == 52
    new_card = new_deck.deal_card()
    assert len(new_deck.cards) == 51
    assert isinstance(new_deck, Deck) == True
    assert isinstance(new_card, Card) == True


def test_player_class():
    new_player = Player()
    assert len(new_player.hand) == 0
    new_deck = Deck()
    new_card = new_deck.deal_card
    new_player.take_card(new_card)
    assert len(new_player.hand) == 1


def test_shoe_class():
    new_shoe = Shoe(2)
    assert len(new_shoe.cards) == 104
    new_card = new_shoe.deal_card
    assert len(new_shoe.cards) == 103
    assert isinstance(new_shoe, Shoe) == True
    assert isinstance(new_card, Card) == True
