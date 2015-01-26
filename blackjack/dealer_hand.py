from blackjack.card import Card


class DealerHand:
    """Current card count.

    Responsibilities:

    * Sums cards in hand
    * Contains action possibilities
        if < 17 == hit
        elif > 17 and < 22 == stay
        else:  bust

    Collaborators:

    * Receives Card from Deck
    * Sends results to Game_manager class"""

    def __init__(self, cards, card_count=0):
        self.cards = cards
        self.card_count = card_count

    def __str__(self):
        return "{}".format(self.cards)

    def dealer_card_count(self, cards):
        """This function manages the card valuation process for the dealer.
        cards = the dealer's hand """

        self.card_count = 0
        for card in cards:
            if card.rank in (2, 3, 4, 5, 6, 7, 8, 9, 10):
                self.card_count += card.rank
            elif card.rank in ('King', 'Queen', 'Jack'):
                self.card_count += 10
            else:
                self.card_count += 1
        for left_card in cards:
            if left_card.rank == 'Ace':
                if self.card_count <= 11:
                    self.card_count += 10
        return self.card_count

    def dealer_actions(self):
        """This function gives the result of the dealer's hand valuation.
        Results are bust, stay, or hit"""

        if self.card_count >= 22:
            return 'bust'
        elif self.card_count >= 17 and self.card_count <= 21:
            return 'stay'
        else:
            return 'hit'
