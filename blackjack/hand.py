class Hand:

    def __init__(self, cards=[]):
        self.cards = cards

    def add_cards(self, card):
        self.cards.append(card)


    def get_ranks(self):
        card_rank_list = []

        for card in self.cards:
            card_rank_list.append(card.rank)

        return card_rank_list

    def get_value(self):
        hand_value = 0
        for card in self.cards:
            hand_value += card.value

        if ((hand_value > 21 and "A" in self.get_ranks()) or
            hand_value <= 11 and "A" in self.get_ranks()):
            for card in self.cards:
                if hand_value > 21 and card.value == 11:
                    card.swap_ace()
                    hand_value = self.get_value()
                elif hand_value <= 11 and card.value == 1:
                    card.swap_ace()
                    hand_value = self.get_value()
        return hand_value
