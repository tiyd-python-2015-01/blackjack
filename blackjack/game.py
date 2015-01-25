from player import Player
from dealer import Dealer
from deck import Deck


class Game:
    """The game keeps track of the deck, player, and dealer, and runs the
       game loop."""

    def __init__(self):
        self.dealer = Dealer()
        self.player = Player()

    def get_correct_game_input(self):
        while True:
            user_choice = input("Hit or Stand? ").lower()
            if user_choice == "hit" or user_choice == "h":
                return "h"
                break
            if user_choice == "stand" or user_choice == "s":
                return "s"
                break

    def side_rules_input(self):
        user_choice = input("Initiate side rules? Y/N ").lower()
        if user_choice == "y":
            print("Ha, no.")

    def wrap_up_round(self):
        self.player.dump_cards()
        self.dealer.dump_cards()
        print("You have: {}".format(self.player.show_money()))


    def play(self):
        continue_game = True
        print("Welcome to Blackjack!")
        while continue_game:
            deck = Deck()
            deck.shuffle()
            blackjack = False
            self.player.deal(deck)
            self.dealer.deal(deck)
            self.dealer.show_first_card()
            self.player.show_cards()
            # self.side_rules_input()
            if not self.player.has_blackjack():
                while not self.player.is_bust():
                    choice = self.get_correct_game_input()
                    if choice == "h":
                        self.player.hit_from_deck(deck)
                        self.player.show_cards()
                    elif choice == "s":
                        break
            else:
                blackjack = True
                print ("You have blackjack!")
            if self.player.is_bust():
                print("You bust!")
                self.player.lose_money()
                self.wrap_up_round()
                if self.player.is_broke():
                    print("You're all out of money! You lose!")
                    continue_game = False
                continue
            self.dealer.show_cards()
            if not self.dealer.has_blackjack() and not blackjack:
                while self.dealer.choose_to_hit():
                    print("The dealer hits!")
                    self.dealer.hit_from_deck(deck)
                    self.dealer.show_cards()
            else:
                print("The dealer has blackjack!")
            if self.dealer.is_bust():
                print("The dealer busts!")
                print("You win!")
                self.player.win_money()
            elif self.player.get_value() > self.dealer.get_value():
                print("You win!")
                if blackjack:
                    self.player.blackjack()
                else:
                    self.player.win_money()
            elif self.player.get_value() == self.dealer.get_value():
                print("Push!")
            else:
                print("You lose!")
                self.player.lose_money()
            self.wrap_up_round()
            if self.player.is_broke():
                print("You're all out of money! You lose!")
                continue_game = False


if __name__ == '__main__':
    game = Game()
    game.play()
