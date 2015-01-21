from class_card import Card
from class_deck import Deck
from class_player_hand import Player_hand
from class_dealer_hand import Dealer_hand

def test_has_fifty_two_cards():
    assert len(Card.card_list) == 52

def test_correct_card_sample():
    assert Card.card_list[0] == ('King', 'Heart')
    assert Card.card_list[1] == ('Queen', 'Heart')
    assert Card.card_list[51] == (10, 'Diamond')

def test_shuffle_count():
    decks = 3
    shuffled = len(Deck.shuffle_deck(decks))
    assert shuffled == (decks * 52)
    assert shuffled != Card.card_list

def test_deal_cards_removed_dealt():
    decks = 3
    shuffled = Deck.shuffle_deck(decks)
    dealt_cards, shuffled_cards = Deck.deal_cards(2, shuffled,
                                                  2)
    assert len(dealt_cards) == 4
    assert len(shuffled) == ((3 *52) - len(dealt_cards))
