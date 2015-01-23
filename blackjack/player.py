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
        self.potential_values = []
        self.cash = 100
        self.blackjack = False

    def get_hand(self,new_cards):
        """receives a list of Cards and stores as players cards"""
        self.cards = new_cards

    def get_card(self,new_card):
        self.cards.append(new_card)

    def display_hand(self):
        # try:
        #     hand = ""
        #     for card in self.cards:
        #         hand += str(card)+"\n"
        #     return hand[0:-1]
        # except:
        #     return "Player has an empty hand."
        return self.cards

    def assess_hand(self):
        value = 0
        ace_count = 0
        for card in self.cards:
            try:
                if 2 <= card.rank <= 10:
                    value += card.rank
            except:
                if card.rank in ["King","Queen","Joker"]:
                    value += 10
                elif card.rank == "Ace":
                    value += 11
                    ace_count +=1
        while ace_count > 0:
            if value > 21:
                value -= 10
            ace_count -= 1
        return value

    def busted(self):
        return self.assess_hand() > 21

    def is_blackjack(self):
        if self.assess_hand() == 21:
            self.blackjack = True
        else:
            self.blackjack = False
        return self.blackjack



class Dealer(Player):
    def __init__(self):
        super().__init__()

    def display_hand(self):
        return self.cards[1:]

    def display_entire_hand(self):
        return self.cards

    def hit_or_stand(self):
        return self.assess_hand() <=17


class Hand:
    def __init__(self):
        self.cards = []
        self.potential_values = []
