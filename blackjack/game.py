from blackjack.deck import Shoe
from blackjack.player import Player
from blackjack.dealer import Dealer
from blackjack.functions import*
from blackjack.interface import*


class Game:

    """
    Have the methods for going through a turn. When initialized it
    runs through the game loop. It interacts with the deck, player and dealer
    class, and pulls from functions and interface.
    """

    def start(self):
        """Initiates the player and dealer objects that will be used for
        the game."""
        self.player = Player()
        self.dealer = Dealer()
        self.pot = 0
        self.side_bet = 0
        start_game()

    def game_setup(self):
        """Sets the board for each game by creating a new shoe, and then
        dealing a card to the player a card to the dealer, and then another
        card to the player, and finally a facedown card to the dealer."""
        self.deck = Shoe(6)
        initial_draw(self.player, self.dealer, self.deck)
        self.pot = ask_for_bet(self.player.money)
        self.player.make_bet(self.pot)
        show_table(self.player, self.dealer, self.pot)
        while True:
            self.surrender_option = early_surrender()
            if self.surrender_option:
                break
            if is_ace(self.dealer.hand):
                if bet_insurance_choice():
                    self.side_bet = insurance_bet(self.pot)
                    self.player.make_bet(self.side_bet)
            break

    def check_for_blackjack(self):
        """A phase of the game where the game checks if the dealer or player
        has Blackjack, and to deal with insurance."""
        if (self.dealer.hand.value + self.dealer.face_down.value) == 21:
            if self.player.hand.value == 21:
                won_insurance_bet(self.side_bet * 2)
                self.player.get_money(self.side_bet)
                self.dealer.reveal()
                push(self.dealer.hand.value, self.player.hand.value)
                self.player.get_money(self.pot)
                return True

            else:
                won_insurance_bet(self.side_bet * 2)
                self.player.money += (self.side_bet * 2)
                self.dealer.reveal()
                dealer_blackjack_win(self.dealer.hand, self.player.hand,
                                     self.pot)
                return True

        if self.player.hand.value == 21:
            lost_insurance_bet(self.side_bet)
            player_win_text(self.pot * (2.5))
            self.player.get_money(self.pot * (2.5))
            return True
        return False

    def player_turn(self):
        """Goes through the player's turn. First asks the player to make
        a wager. It doesn't let the player bet more money than he has. The
        player is then asked to stand or hit. If he hits he is given a card,
        if he stands his turn stops. If he busts while hitting his turn ends
        and automatically loses."""
        while self.player.hand.value < 22:
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
        if not blkjck_chk(self.dealer.hand):
            while self.dealer.hand.value < 17:
                self.dealer.take_card(self.deck)
                show_table_later(self.player, self.dealer, self.pot)

    def who_won(self):
        """Goes through the logic to see who won. If the player loses it will
        explain the amount """
        if self.dealer.hand.value > 21:
            dealer_busts(self.pot)
            self.player.get_money(self.pot * (2))

        elif self.dealer.hand.value > self.player.hand.value:
            dealer_win(self.dealer.hand, self.player.hand,
                       self.pot)

        elif self.dealer.hand.value == self.player.hand.value:
            push(self.dealer.hand.value, self.player.hand.value)
            self.player.get_money(self.pot)

        else:
            player_win_text(self.pot * (2))
            self.player.get_money(self.pot * (2))

    def reset_table(self):
        """Clears the hands of the player and dealer, and pot and side bet."""
        self.player.hand.clear_hand()
        self.dealer.hand.clear_hand()
        self.side_bet = 0
        self.pot = 0

    def __init__(self):
        """Goes through the main game loop."""
        self.start()
        while True:
            while True:
                self.game_setup()
                if self.surrender_option:
                    early_surrender_text((self.pot / 2))
                    self.player.get_money((self.pot / 2))
                    break
                if self.check_for_blackjack():
                    break
                self.player_turn()
                if self.player.hand.value > 21:
                    bust_lose_text(self.pot)
                    break
                self.dealer_turn()
                self.who_won()
                break
            if self.player.money > 0:
                if not play_again():
                    break
            elif self.player.money == 0:
                no_more_money()
                break
            self.reset_table()
