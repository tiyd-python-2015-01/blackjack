

class Pot():

    def __init__(self,purse):
        self.purse= purse
        self.bet = 0


    def make_bet(self,bet_amount):
        """Takes ten credits from player at beggining of game for the bet."""
        self.bet = bet_amount
        #self.purse -= self.bet


    def return_bet(self):
        """returns double the bet"""
        self.purse += self.bet

    def subtract_bet(self):
        """returns double the bet"""
        self.purse -= self.bet
