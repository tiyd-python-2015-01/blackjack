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

def test_correct_card_dealing_to_player():
    new_cards = Player_hand(['10 of Diamond', '5 of Club'])
    assert new_cards.cards == ['10 of Diamond', '5 of Club']

def test_deal_player_cards():
    fresh_deck = Deck()
    new_cards = Player_hand([fresh_deck.deal_card(), fresh_deck.deal_card()])
    assert new_cards.cards is not None

def test_player_card_count():
    fresh_deck = Deck()
    new_cards = Player_hand([fresh_deck.deal_card(), fresh_deck.deal_card()])
    assert new_cards.player_card_count(new_cards.cards) >= 2
