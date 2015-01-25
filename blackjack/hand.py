from blackjack.card import Card
from blackjack.deck import Deck


class Hand:
    """ A hand (either for player or dealer) that can contain cards

    Responsibilities:
    * keep track of which cards are in the hand
    * keep track of the value of the hand


    Collaborators:
    * get popped cards from the shoe"""

    def __init__(self, value=0):
        self.cards = []
        self.value = value

    def _str__(self):
        card_list = [str(card) for card in self.cards]
        return ', '.join(card_list)

    def __repr__(self):
        return self.__str__()

    def get_card(self, deck):
        """gets a card from the deck, adds it to the hand"""
        card = deck.draw()
        return self.cards.append(card)

    def new_card(self):
        """shows the card most recently added to the deck"""
        newest_card = self.cards[-1]
        return newest_card

    def valuation(self):
        """determines the value of the hand, accounting for the
        changing value of Aces, depending on the total hand value"""
        value_dict = {'1': 1,
                      '2': 2,
                      '3': 3,
                      '4': 4,
                      '5': 5,
                      '6': 6,
                      '7': 7,
                      '8': 8,
                      '9': 9,
                      '10': 10,
                      'J': 10,
                      'Q': 10,
                      'K': 10,
                      'A': 11}

        list_of_a = [card.rank for card in self.cards if card.rank == 'A']
        a_counter = len(list_of_a)

        hand_ranks = [card.rank for card in self.cards]
        values = [value_dict[x] for x in hand_ranks]
        value = sum(values)

        while a_counter > 0:
            if value > 21:
                value -= 10
            a_counter -= 1

        return value
