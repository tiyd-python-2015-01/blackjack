from class_card import Card
from class_deck import Deck
from class_player_hand import Player_hand
from class_dealer_hand import Dealer_hand

def test_correct_card_num():
    assert len(Card.card_list) == 52
