"""
Player
    Responsibilities:
        -Name   -Hand   -Makes choices each turn?
    Collaborators
        -Game   -Hand   -Game_State

Dealer
    Responsibilities:
        -Stores Hand    -Plays by set of rules
    Collaborators
        -Hand   -Player     -Game

Human_Player
    Responsibilities:
        -Stores Hand    -Plays according to user input
    Collaborators
        -Hand   -Player     -Game

Hand
    Responsibilites:
        -Store list of cards in hand
    Collaborators
        -Player         -Card       -Game
"""


class Player:
    def __init__(self):
        self.cards = []
        self.cash = 100
        self.blackjack = False

    def get_hand(self, new_cards):
        """ Receives a list of Cards and stores as players cards"""
        self.cards = new_cards

    def get_card(self, new_card):
        """ Adds card to player's list of cards. """
        self.cards.append(new_card)

    def display_hand(self):
        """ Returns cards for interface to display.  """
        return self.cards

    def assess_hand(self):
        """ Assesses value of hand by counting number of aces as it adds the
        values of all the other cards.  If the hand busts and there exists an
        Ace, use the value of 1 rather than 11 by deducting 10 from the hand
        value. """
        value = 0
        ace_count = 0
        for card in self.cards:
            try:
                if 2 <= card.rank <= 10:
                    value += card.rank
            except:
                if card.rank in ["King", "Queen", "Jack"]:
                    value += 10
                elif card.rank == "Ace":
                    value += 11
                    ace_count += 1
        while ace_count > 0:
            if value > 21:
                value -= 10
            ace_count -= 1
        return value

    def busted(self):
        """ Returns True if the hand has busted. """
        return self.assess_hand() > 21

    def is_blackjack(self):
        """ If there are only two cards in the hand and its value is 21, it's
        considered a blackjack.  This is used to determine the winner, later
        in the game. """
        if self.assess_hand() == 21:
            self.blackjack = True
        else:
            self.blackjack = False
        return self.blackjack


class Dealer(Player):
    def __init__(self):
        """ Initialize the dealer as you would any player. """
        super().__init__()

    def display_hand(self):
        """ Dealer shows all but one cards on a typical display.  """
        return self.cards[1:]

    def display_entire_hand(self):
        """ Only called at the end of the game. This shows the dealer's entire
        hand. """
        return self.cards

    def hit_or_stand(self):
        """ Return True to hit (get another card)
        else False to stand.
        If hand is less than 17 or was dealt a soft 17, Hit"""
        if self.assess_hand() < 17:
            return True
        elif (len(self.cards) == 2 and self.assess_hand() == 17 and
              (self.cards[0].rank == "Ace" or self.cards[1].rank == "Ace")):
            return True
        else:
            return False
