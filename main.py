from game import Game
from card import Card
from shoe import Shoe
from hand import Hand
from player import Player
from dealer import Dealer


name = input("Please enter your name: ")

dealer = Dealer()
player = Player(name)
shoe = Shoe(6)
game = Game(dealer, player, shoe)
game_loop = True

game.shoe.shuffle() #intial shuffle

while game_loop:

    if len(shoe._cards) < 26: #shoe gets shuffled when it reaches 26 cards left
        shoe.shuffle()
        print("Shuffling the shoe")

    game.new_turn()

    print("You have {} dollars".format(game.player.stack))
    print("How much would you like to bet?")
    bet_amount = game.place_bet(input("> "))

    game.dealer.show_hand() #initial hands are shown
    game.player.show_hand()

    if game.dealer.hand.hand[1].rank == 'A':
        print("insurance wager?(type 0 for none): ")
        insurance = game.insurance(input("> "), bet_amount)
        while insurance == "more than half":
            insurance = game.insurance(input("> "), bet_amount)

    if dealer.hand.best_hand != 21:
        hit = game.hit_or_stand_with_surrender_and_double()

        while hit == 'h': #player hits
            game.player.hit(game.shoe)
            game.player.show_hand()
            if game.player.hand.best_hand < 21:
                hit = game.hit_or_stand()

        if hit == 'd': #player doubles down
            game.player.bet(bet_amount)
            game.player.hit(game.shoe)

        if hit == 'u': #player surrenders
            game.player.stack += round(game.pot / 2)

        #the hand is played out
        if not hit == 'u' and game.player.bust:
            game.dealer.play_out_hand(game.shoe)
            game.dealer.reveal_hand()
            game.player.show_hand()
            if game.dealer.hand.best_hand > 21:
                print("Dealer busts!, you win!")
                game.player.stack += game.pot * 2
            else:
                game.check_for_winner(game.dealer, game.player)


    else: #dealer has 21
        game.dealer.reveal_hand()
        if player.hand.best_hand == 21 and dealer.hand.best_hand == 21:
            print("push!")
            game.player.stack += game.pot
        elif dealer.hand.best_hand == 21: #dealer blackjack
            print("Dealer has blackjack! You lose!")
        else: #player busts
            print("Your hand is over 21, you lose!!")

    if player.stack < 1: #check to see player has money remaining
        print("You are out of money! Game over!")
        break

    game_loop = game.play_again()
