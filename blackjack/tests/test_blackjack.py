from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.player_hand import Player_hand
from blackjack.dealer_hand import Dealer_hand


def test_correct_card_output():
    new_card = Card('King', 'Diamonds')
    assert new_card.suit == 'Diamonds'
    assert new_card.rank == 'King'


def test_deck_fifty_two_cards():
    assert len(Deck()) == 52


def test_shuffle_count():
    straight_deck = Deck()
    shuffled_cards = Deck()
    shuffled_cards.shuffle_deck()
    assert len(shuffled_cards) == 52
    assert straight_deck != shuffled_cards


def test_deal_card_removes_it():
    deck = Deck()
    card = deck.deal_card()
    assert card is not None
    assert len(deck) ==51
