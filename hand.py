class Hand:
    """An assortment of cards

    Responsibilitites:

    * Can hold x cards
    * Has a hard or soft total for hand, aces depend on hand
    * Can add cards to hand
    * Check if hand is busted (over 21)

    Collaborators:

    * A Hand is made up of Cards
    * A Player and Dealer can hold a hand
    * The shoe can deal to the hand
    """

    def __init__(self, hand):
        self.hand = hand

    @property
    def hard_total(self):
        hard_total = 0
        for card in self.hand:
            if type(card.rank) == str:
                if card.rank == 'A':
                    hard_total += 11
                else:
                    hard_total += 10
            else:
                hard_total += card.rank
        return hard_total

    @property
    def soft_total(self):
        soft_total = 0
        for card in self.hand:
            if type(card.rank) == str:
                if card.rank == 'A':
                    soft_total += 1
                else:
                    soft_total += 10
            else:
                soft_total += card.rank
        return soft_total

    @property
    def best_hand(self):
        if self.hard_total > 21:
            return int(self.soft_total)
        else:
            return int(self.hard_total)

    def bust(self):
        return self.soft_total > 21

    def draw(self, deck):
        card = deck.draw()
        self.hand.append(card)

    def new_hand(self, deck):
        self.draw(deck)
        self.draw(deck)

    def reset_hand(self):
        self.hand = []

    def __str__(self):
        hand_list = [str(card) for card in self.hand]
        return str(', '.join(hand_list))

    def __repr__(self):
        return self.__str__()
