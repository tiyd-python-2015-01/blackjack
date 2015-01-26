

class Pot():
    """Makes bets, holds total money and adds and subtracts from total."""
    
    def __init__(self, purse):
        self.purse = purse
        self.bet = 0

    def make_bet(self, bet_amount):
        """Takes ten credits from player at beggining of game for the bet."""
        self.bet = bet_amount

    def return_bet(self):
        """Adds the bet amount to the purse the bet"""
        self.purse += self.bet

    def subtract_bet(self):
        """Subtracts the bet from the purse"""
        self.purse -= self.bet
