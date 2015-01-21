class Card:
    """A playing card.

    Responsibilities:

    * Has a rank and a suit.
    * Has a point value. Aces point values depend on the Hand.

    Collaborators:

    * Collected into a Deck.
    * Collected into a Hand for each player and a Hand for the dealer.
    """

    card_list = []
    num_cards = range(2, 11)
    face_cards = ['King', 'Queen', 'Jack', 'Ace']
    suits = ['Heart', 'Club', 'Spade', 'Diamond']

    for suit in suits:
        for face in face_cards:
            card_list.append((face, suit))
        for num in num_cards:
            card_list.append((num, suit))

    def __init__(self):
        return self.card_list
