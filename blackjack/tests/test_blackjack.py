from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.player_hand import PlayerHand
from blackjack.dealer_hand import DealerHand
from blackjack.user import User



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
    new_cards = PlayerHand(['10 of Diamonds', '5 of Clubs'])
    assert new_cards.cards == ['10 of Diamonds', '5 of Clubs']

def test_deal_player_cards():
    fresh_deck = Deck()
    new_cards = PlayerHand([fresh_deck.deal_card(), fresh_deck.deal_card()])
    assert new_cards.cards is not None

def test_player_card_count():
    fresh_deck = Deck()
    new_cards = PlayerHand([fresh_deck.deal_card(), fresh_deck.deal_card()])
    assert new_cards.player_card_count(new_cards.cards) >= 2
    assert new_cards.player_card_count(new_cards.cards) <= 22

def test_player_additional_cards_hit():
    fresh_deck = Deck()
    new_cards = PlayerHand([fresh_deck.deal_card(), fresh_deck.deal_card()])
    next_card = PlayerHand(fresh_deck.deal_card())
    new_cards.cards.append(next_card.cards)
    assert len(new_cards.cards) == 3

def test_player_options():
    new_cards = PlayerHand([])
    assert new_cards.player_actions(25) == 'bust'
    assert new_cards.player_actions(21) == '21'
    assert new_cards.player_actions(20) == ('hit', 'stay')

def test_dealer_options():
    new_cards = DealerHand([])
    assert new_cards.dealer_actions(25) == 'bust'
    assert new_cards.dealer_actions(21) == '21'
    assert new_cards.dealer_actions(17) == 'stay'
    assert new_cards.dealer_actions(5) == 'hit'

def test_user_pot_generation():
    user_chips = User()
    assert user_chips.chip_count == 500

def test_user_bet_removes_money():
    user_chips = User()
    assert user_chips.bet_chips(20) == 480
