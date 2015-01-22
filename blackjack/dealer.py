class Dealer:
    """A computer player that uses an algorithm to determine whether to hit
    or stay

    Responsibilities:
    * Stay on 17 (with no Ace in hand)
    * Hit on 17 (with Ace in hand)
    * Hit on 16 or under
    * Stay on 18-21

    Collaborators:
    * on hit, tell dealer's Hand to get Card from Shoe
    * """
