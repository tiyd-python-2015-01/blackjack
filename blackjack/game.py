class Game:
    """Stores Information about a Game
    Responsibilities:
    * Keeps information in a list of the winners of each game: Dealer, Player, Push
    * gets_winner() to get information on who won the game
    * set_winner() to update list with new winner
    Collaborators:
    * Dealer, Player"""

    def __init__(self):
        self.winners = []

    def set_winner(self, whowon):
        self.winners.append(whowon)

    def get_winners(self):
        return self.winners

    def __repr__(self):
        return "{}".format(self.winners)

    def __str__(self):
        return "{}".format(self.winners)
