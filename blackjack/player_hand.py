from blackjack.card import Card


class PlayerHand:
    """current card count.

    Responsibilites:
        *sum cards in hand
        *holds the possibilites of action
            hit
            stay
            double down
            split
            if >= 22 == bust

    Collaboraters:
        *Recieves card from deck
        *Gives actionable choices to player"""

    def __init__(self, cards, count = 0):
        self.cards = cards
        self.count = count

    def __str__(self):
        return "{}".format(self.cards)

    def player_card_count(self, cards):
        self.count = 0
        for card in cards:
            if card.rank in (2, 3, 4, 5, 6, 7, 8, 9, 10):
                self.count += card.rank
            elif card.rank in ('King', 'Queen', 'Jack'):
                self.count += 10
            else:
                self.count += 1
        for left_card in cards:
            if left_card.rank == 'Ace':
                if self.count <= 11:
                    self.count += 10
        return self.count

    def player_actions(self):
        if self.count >= 22:
            return 'bust'
        elif self.count == 21:
            return '21'
        else:
            return 'choice'
        # double down
        # split
