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
        """Adding a method so a card may be added to a hand."""
        self.cards.append(card)


    def remove(self):
        """Adding a method so a card may be removed from a hand."""
        self.cards.pop()

    def value_check(self):
        """Checks to see what the value of a hand is. Goes through the whole hand
        and finds the values of each card other than an ace"""
        face_cards = ["Jack", "Queen", "King"]
        hand_value = 0
        for card in self.cards:
            if card.rank.isdigit():
                hand_value += int(card.rank)
            elif card.rank in face_cards:
                hand_value += 10
        for card in self.cards:
            if card.rank == "Ace":
                if hand_value > 10:
                    hand_value += 1
                else:
                    hand_value += 11
        return hand_value
