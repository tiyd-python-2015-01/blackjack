class Player_hand:
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


    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Your cards our\n{}".format(self.cards)

    def player_card_count(self, cards):
        count = 0
        for card in cards:
            if card.rank in(2,3)



    #def initial_hand(self):
    #    initial_hand = sum([cards.points() for cards in self])
    #    aces = len([card for card in self if card == card.rank == 'A'])
    #    # implement ace logic here
    #    score = initial_hand - max(0,10*min(int((initial_hand-22)/10)+1, aces))
    #    return score
