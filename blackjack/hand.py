class Hand:
    def __init__(self):
        self.cards = []


    def __str__(self):
        return "Your hand consists of {}.".format(self.cards)


    def __repr__(self):
        return self.__str__()


    def __len__(self):
        return len(self.cards)


    def add(self, card):
        self.cards.append(card)
