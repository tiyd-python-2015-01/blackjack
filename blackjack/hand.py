class Hand:

    def __init__(self):
        self.cards = []

    def __str__(self):
        return "consists of {}.".format(self.cards)

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.cards)

    def add(self, card):
        """Adding a method so a card may be added to a hand."""
        self.cards.append(card)

    def remove(self):
        """Adding a method so a card may be removed from a hand."""
        return self.cards.pop()

    @property
    def value(self):
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

    def clear_hand(self):
        """A way to get rid of cards inbetween games."""
        self.cards = []

    def check_bust(self):
        """A way of seeing if a hand has busted."""
        return self.value > 21

    def blackjack(self):
        """A way of seeing if a hand has blackjack."""
        return len(self.cards) == 2 and self.value == 21

    def is_ace(self):
        """A way of seeing if a hand has an Ace."""
        return len(self.cards) == 1 and self.value == 11
