from player import Player
from dealer import Dealer
from deck import Deck


class Game:
    """The game keeps track of the deck, player, and dealer, and runs the
       game loop."""

    def __init__(self):
        self.dealer = Dealer()
        self.player = Player()


    def play(self):
        continue_game = True
        while continue_game:
            deck = Deck()
            deck.shuffle()
            self.player.deal(deck)
            self.dealer.deal(deck)
            self.dealer.show_first_card()
            self.player.show_cards()
            user_choice = input("Initiate side rules? Y/N")
            if user_choice == "Y":
                print("Ha, no.")
            user_choice = input("")
            continue_game = False


if __name__ == '__main__':
    game = Game()
    game.play()
