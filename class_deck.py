from class_card import Card
import random


class Deck:
    """A deck of cards.

    Responsibilities:

    * Has a collection of cards
    * Shuffles cards
    * Deals out cards

    Collaborators:

    * Collected from card class.
    * Deals cards to Dealer_hand and Player_hand class """


    def shuffle_deck(num_of_decks = 3):

        shuffled_list = Card.card_list * num_of_decks
        random.shuffle(shuffled_list)

        return shuffled_list

    def deal_cards(num_cards, shuffled_deck, num_players):

        dealt_cards = []
        for num in range(num_players):
            for num in range(num_cards):
                dealt_cards.append(shuffled_deck.pop())

        return dealt_cards, shuffled_deck


# print(Deck.shuffle_deck())
#print(Deck.deal_cards(2, Deck.shuffle_deck(), 2))
#Dealer gets 1st card down. Rest are face up.
