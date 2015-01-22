from class_card import Card
from player_hand import Player_hand
import random

class Deck:
    """a deck of cards

    Responsibilites:

    *holds collection of cards
    *shuffles cards
    *deals cards
    *dealer gets first card down

    Collaboraters:

    *collected from card class
    *deals cards to Hand"""

    def shuffle_deck(num_of_decks = 3):
        shuffled_list = Card.card_list * num of decks
        random.shuffle(shuffled_list)
        return shuffled_list

    def deal_cards(num_cards):

        for num in num cards:

        player_hand.card1 = shuffled_deck.pop()
        player_hand.card2 = shuffled_deck.pop()
        dealer_hand.card1 = shuffled_deck.pop()
        dealer_hand.card2 = shuffled_deck.pop()
        print(player_hand.card1, player_hand.card2)
        return True

print(Deck.deal_cards(2, Deck.huffle_deck()))
print(Deck.shuffle_deck())
