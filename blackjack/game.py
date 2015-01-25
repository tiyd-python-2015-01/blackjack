from deck import Shoe
from player import Player
from dealer import Dealer
from functions import*
from interface import*


class Game:

    """
    Have the methods for going through a turn. When initialized it
    runs through the game loop. It interacts with the deck, player and dealer
    class, and pulls from functions and interface.
    """

    def reset_table(self):
        """Clears the hands of the player and dealer."""
        self.player.hand.clear_hand()
        self.dealer.hand.clear_hand()

    def start(self):
        """Initiates the player and dealer objects that will be used for
        the game."""
        self.player = Player()
        self.dealer = Dealer()
        start_game()

    def game_setup(self):
        """Sets the board for each game by creating a new shoe, and then
        dealing a card to the player a card to the dealer, and then another
        card to the player, and finally a facedown card to the dealer."""
        self.deck = Shoe(6)
        self.player.take_card(self.deck)
        self.dealer.take_card(self.deck)
        self.player.take_card(self.deck)
        self.dealer.put_face_down(self.deck)

    def player_turn(self):
        """Goes through the player's turn. First asks the player to make
        a wager. It doesn't let the player bet more money than he has. The
        player is then asked to stand or hit. If he hits he is given a card,
        if he stands his turn stops. If he busts while hitting his turn ends
        and automatically loses."""
        self.pot = ask_for_bet(self.player.money)
        self.player.make_bet(self.pot)

        show_table(self.player, self.dealer, self.pot)
        self.surrender_option = early_surrender()
        while self.player.hand.value < 22:
            if self.surrender_option:
                break
            choice = player_choice()
            if choice == "S":
                break
            elif choice == "D":
                self.player.take_card(self.deck)
                self.player.make_bet(self.pot)
                self.pot += self.pot
                break
            else:
                self.player.take_card(self.deck)
            show_table(self.player, self.dealer, self.pot)

    def dealer_turn(self):
        """Goes through the blackjack dealer mechanics. Shows the face down
        card and then the checks to see if the dealer has blackjack. Checks to
        see if the value of the hand is less than 17, if so the dealer draws
        a card."""
        self.dealer.reveal()
        show_table_later(self.player, self.dealer, self.pot)
        print(self.dealer.hand)
        if not blkjck_chk(self.dealer.hand):
            while self.dealer.hand.value < 17:
                self.dealer.take_card(self.deck)
                show_table_later(self.player, self.dealer, self.pot)

    def who_won(self):
        """Goes through the logic to see who won. If the player loses it will
        explain the amount """
        if blkjck_chk(self.player.hand) and blkjck_chk(self.dealer.hand):
            push(self.dealer.hand.value, self.player.hand.value)
            self.player.get_money(self.pot * (2))

        elif blkjck_chk(self.dealer.hand):
            dealer_win(self.dealer.hand.value, self.player.hand.value,
                       self.pot)

        elif blkjck_chk(self.player.hand):
            blackjack_text()
            player_win_text(self.pot * (2))
            self.player.get_pot(self.pot * (2))

        elif self.dealer.hand.value > 21:
            dealer_busts(self.pot)
            self.player.get_money(self.pot * (2))

        elif self.dealer.hand.value > self.player.hand.value:
            dealer_win(self.dealer.hand.value, self.player.hand.value,
                       self.pot)

        elif self.dealer.hand.value == self.player.hand.value:
            push(self.dealer.hand.value, self.player.hand.value)
            self.player.get_money(self.pot)

        else:
            player_win_text(self.pot * (2))
            self.player.get_money(self.pot * (2))

    def __init__(self):
        self.start()
        while True:
            while True:
                self.game_setup()
                self.player_turn()
                if self.surrender_option:
                    early_surrender_text((self.pot / 2))
                    self.player.get_money((self.pot / 2))
                    break
                if self.player.hand.value > 21:
                    bust_lose_text(self.pot)
                    break
                self.dealer_turn()
                self.who_won()
                break
            if self.player.money > 0:
                if not play_again():
                    break
            else:
                break
            self.reset_table()
Game()
