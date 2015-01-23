from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.deck import Shoe
from blackjack.player import Player
from blackjack.functions import value_checker


def test_card_class():
    card_1 = Card("10", "Spades")
    assert card_1.suit == "Spades"
    assert card_1.rank == "10"


def test_deck_class():
    new_deck = Deck()
    assert len(new_deck.cards) == 52
    new_card = new_deck.deal_card()
    assert len(new_deck.cards) == 51


def test_player_class():
    new_player = Player()
    assert len(new_player.hand) == 0
    new_deck = Deck()
    new_player.hit(new_deck)
    assert len(new_deck) == 51
    assert len(new_player.hand) == 1


def test_shoe_class():
    new_shoe = Shoe(2)
    assert len(new_shoe) == 104
    new_card = new_shoe.deal_card()
    assert len(new_shoe) == 103


def test_value_checker():
    first_hand = [Card("Queen", "Hearts"), Card("7", "Clubs")]
    assert value_checker(first_hand) == 17
    second_hand = [Card("Ace", "Spades"), Card("Queen", "Clubs"),
                   Card("2", "Hearts" )]
    assert value_checker(second_hand) == 13
    third_hand = [Card("Ace", "Hearts"), Card("4", "Spades")]
    assert value_checker(third_hand) == 15
    ace_hand = [Card("Ace", "Hearts"), Card("Ace", "Clubs"),
    Card("Ace", "Spades"), Card("Ace", "Diamonds")]
    assert value_checker(ace_hand) == 14
