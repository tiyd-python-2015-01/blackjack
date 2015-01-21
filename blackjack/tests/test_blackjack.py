import class_card
from class_deck import Deck
from class_player_hand import Player_hand
from class_dealer_hand import Dealer_hand


def test_correct_card_output():
    new_card = class_card.Card('King', 'Diamonds')
    assert new_card.suit == 'Diamonds'
    assert new_card.rank == 'King'

def test_deck_fifty_two_cards():
    fresh_deck = Deck()
    assert len(fresh_deck.card_deck) == 52

def test_correct_object_type_deck():
    fresh_deck = Deck()
    assert type(fresh_deck.card_deck) == list
    assert type(fresh_deck) == Deck

def test_shuffle_count():
    fresh_deck = Deck()
    fresh_deck_count = len(fresh_deck.shuffle_deck)
    assert fresh_deck.shuffle_deck == 52
    assert fresh_deck.shuffle_deck != fresh_deck

def x_test_deal_cards_removed_dealt():
    decks = 3
    shuffled = Deck.shuffle_deck(decks)
    dealt_cards, shuffled_cards = Deck.deal_cards(2, shuffled,
                                                  2)
    assert len(dealt_cards) == 4
    assert len(shuffled) == ((3 *52) - len(dealt_cards))
