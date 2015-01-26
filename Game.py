class Game:
    """Information about the game.

    Responsibilities:

    * Check for winner
    * Handles betting and bankroll
    * Resets the game and hands

    Collaborators

    * Checks the player and dealer's hand amounts and compares them
    """

    def __init__(self, dealer, player, shoe):
        self.dealer = dealer
        self.player = player
        self.shoe = shoe
        self.pot = 0

    def play_again(self):
        choice = input('Press "p" to play again or "q" to quit: ').lower()
        return choice == 'p'

    def hit_or_stand_with_surrender_and_double(self):
        choice = input('[H]it, [S]tand, [D]ouble, or S[u]rrender: ').lower()
        if choice in 'hsdu':
            return choice
        else:
            print("Invalid input!")
            return self.hit_or_stand()

    def hit_or_stand(self):
        choice = input('[H]it, [S]tand: ').lower()
        if (choice == 'h') or (choice == 's'):
            return choice
        else:
            print("Invalid input!")
            return self.hit_or_stand()

    def dealer_has_blackjack(self):
        return self.dealer.hand.hard_total == 21

    def player_has_blackjack(self):
        return self.player.hand.hard_total == 21

    def check_for_winner(self, dealer, player):
        self.dealer.reveal_hand()
        self.player.show_hand()
        if self.dealer.hand.bust():
            print("Dealer busted! You win!")
            self.player.stack += self.pot * 2
        else:
            if self.player.hand.best_hand < self.dealer.hand.best_hand or self.player.hand.bust():
                print("You Lose")
            elif self.dealer.hand.best_hand < self.player.hand.best_hand:
                print("You Win!")
                self.player.stack += self.pot * 2
            else:
                print("Push!")
                self.player.stack += self.pot

    def new_turn(self):
        self.dealer.hand.reset_hand()
        self.player.hand.reset_hand()
        self.dealer.hand.new_hand(self.shoe)
        self.player.hand.new_hand(self.shoe)
        self.pot = 0

    def place_bet(self, amount):
        try:
            amount = int(amount)
            if amount <= self.player.stack:
                self.player.stack -= amount
                self.pot += amount
                return amount
            else:
                self.place_bet(input("Not enough funds! You have {} dollars. P"
                                     "lace a bet: ".format(self.player.stack)))
        except ValueError:
            self.place_bet(input("Place a bet: "))

    def insurance(self, amount, bet):
        try:
            amount = int(amount)
            if amount != 0:
                if amount > (bet / 2):
                    print("Insurance may not be more than half the bet")
                    return "more than half"
                self.player.stack -= amount
                if self.dealer.hand.hard_total == 21:
                    print("dealer has blackjack")
                    self.player.stack += (amount * 3)
                return amount
        except ValueError:
            return "more than half"
