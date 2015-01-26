from blackjack.hand import Hand

class Player:
    """The player posesses a hand (or more, depending on the rules), and makes
    decisions to bet, to draw cards, and to stand, (among other possibilities)
    as dictated by the user.

    Responsibilities:
    Has one (or more) hands.
    Has money.
    Optionally adds cards to hands during the player's turns.

    Collaborators:
    Is one of two agents contained in the game.
    Has at least one hand.
    """
    def __init__(self, bet=10):
        self.money = 100
        self.hands = []
        self.bet = bet

    def deal(self, deck):
        hand = Hand()
        hand.grab(deck.draw())
        hand.grab(deck.draw())
        self.hands.append(hand)

    def lose_money(self):
        """When called, subtracts the bet from the player's money."""
        self.money -= self.bet

    def win_blackjack(self):
        """When called, increases the player's winnings by the special
           blackjack multipier of the bet"""
        self.money += (self.bet * 1.5)

    def win_money(self):
        """When called, increases the player's winnings by the bet."""
        self.money += self.bet

    def show_cards(self):
        your_hand = self.hands[0]
        card_list = your_hand.show_cards()
        card_string = ", ".join(card_list)
        hand_value = your_hand.value()
        print("You have: {} ({})".format(card_string, hand_value))

    def is_broke(self):
        """Checks to see if the player still has money. Might change to
           check if the player has enough to bet."""
        #print("Has {}, so isbroke is {}".format(self.money, self.money <= 0))
        return self.money <= 0

    def is_bust(self):
        """Tests the player's first hand for bustedness."""
        return self.hands[0].is_bust()

    def dump_cards(self):
        """Empties cards from the player, preventing a zombie game where the
           player never puts down any of their hands."""
        self.hands = []

    def hit_from_deck(self, deck):
        """Takes a card from the given deck."""
        self.hands[0].grab(deck.draw())

    def num_cards(self):
        """Returns the number of cards in the player's hand."""
        cards = 0
        for hand in self.hands:
            cards += hand.num_cards()
        return cards

    def get_value(self):
        """Gets the player's hand's blackjack score."""
        return self.hands[0].value()

    def has_blackjack(self):
        """Checks the player's hand for blackjack."""
        return self.hands[0].is_blackjack()

    def show_money(self):
        """Returns a string representation of the player's money."""
        money_string = "${}".format(self.money)
        return money_string
