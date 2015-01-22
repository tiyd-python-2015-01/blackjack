class Dealer_hand:
    """Current hand count

    Responsibilities:

    *Sums cards in hand
    *Contains action possibilities
        if < 17 == hit
        if > 17 and <22 == stay
        if > 21 == bust

    Collaboraters:

    *Recieves cards from Deck
    *Sends results to Game_manager class"""
