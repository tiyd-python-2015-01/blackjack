from game import Game
from shoe import Shoe
from player import Player
from dealer import Dealer

if __name__ == "__main__":
    name = input("Please enter your name: ")

    dealer = Dealer()
    player = Player(name)
    shoe = Shoe(6)
    game = Game(dealer, player, shoe)
    game_loop = True

    game.shoe.shuffle()  # Intial shuffle

    while game_loop:

        if len(shoe._cards) < 26:  # Shoe gets shuffled when it reaches 26 cards
            shoe.shuffle()
            print("Shuffling the shoe")

        game.new_turn()

        print("You have {} dollars".format(game.player.stack))
        print("How much would you like to bet?")
        bet_amount = game.place_bet(input("> "))

        game.dealer.show_hand()  # Initial hands are shown
        game.player.show_hand()

        # Ask player for insurance when dealer has ace
        if game.dealer.hand.hand[1].rank == 'A':
            print("insurance wager?(type 0 for none): ")
            insurance = game.insurance(input("> "), bet_amount)
            while insurance == "more than half":
                insurance = game.insurance(input("> "), bet_amount)

        # Player has blackjack and dealer does not
        if game.player_has_blackjack():
            if game.dealer_has_blackjack():
                print("Push!")
                game.player.stack += game.pot
            else:
                print("Blackjack! you win!")
                game.player.stack += game.pot * 3

        else:
            player_decision = game.hit_or_stand_with_surrender_and_double()

            while player_decision == 'h':  # Player hits
                game.player.hit(game.shoe)
                game.player.show_hand()
                if game.player.hand.best_hand <= 21:
                    player_decision = game.hit_or_stand()
                else:  # Player busts
                    print("Your hand is over 21, you lose!")
                    break

            if player_decision == 's':  # Player stands
                game.dealer.play_out_hand(game.shoe)
                game.check_for_winner(game.dealer, game.player)

            elif player_decision == 'd':  # Player doubles down
                game.player.hit(game.shoe)
                game.dealer.play_out_hand(game.shoe)
                game.check_for_winner(game.dealer, game.player)

            else:  # Player surrenders
                game.player.stack += round(game.pot / 2)

        if player.stack < 1:  # Check to see player has money remaining
            print("You are out of money! Game over!")
            break

        game_loop = game.play_again()
