from hand import Hand


class Player:
    """Contains the Players bank.

    responsibilties:
    *Contains the method for decrementing the player's bet.
    *Contains the methods for incrementing the players bank based
    on the win/push condition (blackjack or not).

    collaborators:
    *Collected in the game state
    """

    def __init__(self):
        self.bank = 100

    def __str__(self):
        self.hand = ' '.join([cards.__str__() for cards in self.hand])

    def bet(self, bet):
        """Decrements the bet from the player's bank."""
        self.bank -= bet

    def win_no_blackjack(self, bet):
        """Increments non-blackjack winnings to the player's bank."""
        self.bank += bet * 2

    def win_blackjack(self, bet):
        """Increments blackjack winnings to the player's bank."""
        self.bank += bet * 2.5

    def push(self, bet):
        """Return's the player's bet when the result is a push."""
        self.bank += bet
