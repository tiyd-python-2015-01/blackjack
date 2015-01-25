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

    hit = game.hit_or_stand_with_surrender_and_double()

    while hit == 'h' and not game.player.hand.bust(): #player hits
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
    if player.hand.best_hand <= 21 and dealer.hand.best_hand != 21 and not hit == 'u':
        game.dealer.play_out_hand(game.shoe)
        game.dealer.reveal_hand()
        game.player.show_hand()
        if game.dealer.hand.best_hand > 21:
            print("Dealer busts!, you win!")
            game.player.stack += game.pot * 2
        else:
            game.check_for_winner(game.dealer, game.player)

    #game
    elif not hit == 'u':
        game.dealer.reveal_hand()
        if dealer.hand.best_hand == 21:
            print("Dealer has blackjack! You lose!")
        else:
            print("Your hand is over 21, you lose!!")

    else:
        print("You wimp! You get half of your bet back")

    if player.stack < 1:
        print("You are out of money! Game over!")
        break

    game_loop = game.play_again()
