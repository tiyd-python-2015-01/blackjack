class Game:
    """Stores Information about a Game
    Responsibilities:
    * Keeps information about who won the game: Dealer, Player, Push
    * Methods: gets_winner() to get information on who won the game
    Collaborators:
    * Dealer, Player"""

    def __init__(self):
        self.winner = ''

    def set_winner(self, whowon):
        self.winner = whowon

    def get_winner(self):
        return self.winner

    def __repr__(self):
        return "{}".format(self.winner)

    def __str__(self):
        return "{}".format(self.winner)
