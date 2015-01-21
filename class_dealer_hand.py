class Dealer_hand:
    """Current card count.

    Responsibilities:

    * Sums cards in hand
    * Contains action possibilities
        if < 17 == hit
        elif > 17 and < 22 == stay
        else:  bust

    Collaborators:

    * Receives Card from Deck
    * Sends results to Game_manager class"""

    cards = []

    def __init__(self, x, y):
        cards = [x, y]
