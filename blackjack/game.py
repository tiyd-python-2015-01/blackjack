import player
import dealer


class Game:
    """The game keeps track of the deck, player, and dealer, and runs the
       game loop."""

    def __init__(self):
        dealer = Dealer()
        player = Player()


    def play():
        continue = True
        while continue:
            deck = Deck()
            deck.shuffle()
            player.deal(deck)
            dealer.deal(deck)
            dealer.show_first_card()
            continue = False
