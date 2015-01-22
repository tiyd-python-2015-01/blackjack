class Dealer_hand:
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

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "The dealer has {}".format(self.cards)

    def dealer_card_count(self, cards):
        count = 0
        for card in cards:
            if card.rank in (2, 3, 4, 5, 6, 7, 8, 9, 10):
                count += card.rank
            elif card.rank in ('King', 'Queen', 'Jack'):
                count += 10
        for left_card in cards:
            if left_card.rank == 'Ace':
                if count >= 11:
                    count += 1
                else:
                    count += 11
        return count

    def dealer_actions(self, count):
        if count >= 22:
            return 'bust'
        elif count == 21:
            return '21'
        elif count >= 17 and count <= 21:
            return 'stay'
        else:
            return 'hit'
