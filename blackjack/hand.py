class Hand:
    """ Hand class contains the current cards in play for either the player
    or dealer.  It has methods to return the total value of the cards held
    as well as update the value of the Ace based on the current value of
    the hand.

    Responsibilities:
    * Container for Card objects
    * Reporting the combined value of all Card objects held
    * Logic to ensure that Aces are counted as the correct value based on
      the total value of the current hand.

    Interactions:
    * Hand objects are distributed to the player and the dealer.
    * Hand objects receive card objects from the deck.
    """


    def __init__(self, bet, cards=[]):
        self.cards = cards
        self.bet = bet

    def add_cards(self, card):
        """Appends a dealt card to the Hand object's cards list"""
        self.cards.append(card)

    def get_ranks(self):
        """Returns a list of ranks of all cards in the Hand object's
        card list"""
        card_rank_list = []

        for card in self.cards:
            card_rank_list.append(card.rank)

        return card_rank_list

    def get_card_strings(self):
        """Returns a string representation of all cards in the Hand object's
        card list"""
        card_strings = []
        for card in self.cards:
            card_strings.append(str(card))
        cards = "[ " + " ".join(card_strings) + " ]"
        return cards

    def get_value(self):
        """Returns the total value of all cards in the card list"""
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
