from deck import Deck
from card import Card
from player_hand import Player_Hand
from dealer_hand import Dealer_Hand


def test_hit_adds_player_card():
    card1 = Card("Ace", "Diamonds")
    player_hand1 = Player_Hand()
    player_hand1.hit(card1)
    assert player_hand1.hand == [Card("Ace", "Diamonds")]


def test_hit_adds_dealer_card():
    card1 = Card("Ace", "Diamonds")
    dealer_hand1 = Dealer_Hand()
    dealer_hand1.hit(card1)
    assert dealer_hand1.hand == [Card("Ace", "Diamonds")]


def test_draw_two_cards():
    deck1 = Deck()
    hand2 = Player_Hand()
    deck1.shuffle_deck()
    assert len(hand2.hand) == 0
    hand = hand2.draw_two(deck1)
    assert len(hand) == 2


def test_hand_value():
    player1 = Player_Hand([Card(4, "Hearts"), Card("King", "Spades")])
    print(player1.hand)
    assert player1.hand_value() == 14
