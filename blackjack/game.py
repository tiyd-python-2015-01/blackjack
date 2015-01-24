from blackjack.deck import Deck
from blackjack.player import Player
from blackjack.dealer import Dealer
from blackjack.functions import*
from blackjack.interface import*


class Game:

    def start(self):
        self.player = Player()
        self.dealer = Dealer()
        start_game()


    def game_setup(self):
        self.deck = Deck()
        self.player.take_card(self.deck)
        self.dealer.take_card(self.deck)
        self.player.take_card(self.deck)
        self.dealer.put_face_down(self.deck)


    def player_turn(self):
        stand = False
        self.pot = ask_for_bet(self.player.money)
        self.player.make_bet(self.pot)
        while stand == False or self.player.value_check < 22
            show_table(self.player, self.dealer, self.pot)
            choice = hit_or_stand()
            decider(choice, self.player)
        return stand

    def dealer_turn(self):
        self.dealer.reveal()
        show_table(self.player, self.dealer, self.pot)
        if not blackjack_check(self.dealer.hand):
            while dealer.hand.value_check() < 17:
                self.dealer.take_card(self.deck)
                show_table(self.player, self.dealer, self.pot)

    def who_won(self):
        if blkjck_chk(self.player.hand) and blkjck_chk(self.daler.hand):
            # print something about it being a push, get your bet back.
            self.player.get_pot(self.pot)
        elif blkjck_chk(self.dealer.hand):
            #print something about player loses this hand, he loses X amount.
        elif blkjck_chk(self.player.hand):
            #print something about player wins, they receive x amount
            self.player.get_pot(self.pot*(1.5))
        elif self.dealer.hand.value_check() > self.player.hand.value_check():
            #print something about player loses this hand, he loses X amount
        else:
            #print something about player wins this hand, he wins x amount
            self.player.get_pot(self.pot*(1.5))


                self.hand.hit(deck)
                # if check(bust):
                # Make a you lose loop that will explain you lose and
                # subtract the amount you bet from the
            if choice == "S":
                # Now this goes to dealers turn
                dealer.turn(deck)


    def __init__(self):
        self.start()
        while True:
            while True:
                self.game_setup()
                self.player_turn()
                if self.player.hand.value_check() > 21:
                    #print something about player loses this hand, he loses X amount
                    break
                self.dealer_turn()
                self.who_won()
                break
        #Have a function asking if they want to play again?
        if not play_again():
            break
