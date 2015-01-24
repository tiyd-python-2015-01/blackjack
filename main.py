from game import Game
from card import Card
from deck import Deck
from hand import Hand
from player import Player
from dealer import Dealer
import time


name = input("Please enter your name: ")
dealer = Dealer()
player = Player(name)
deck = Deck()
game = Game(dealer, player, deck)
game_loop = True

while game_loop:

    game.new_turn()

    if player.stack < 1:
        print("You are out of money! Game over!")
        break

    print("You have {} dollars".format(game.player.stack))
    print("How much would you like to bet?")
    game.place_bet(input("> "))

    game.dealer.show_hand()
    game.player.show_hand()

    hit = game.hit_or_stand()

    while hit and not game.player.hand.bust():
        game.player.hit(game.deck)
        game.player.show_hand()
        if game.player.hand.best_hand < 21:
            hit = game.hit_or_stand() #player can't bust



    if player.hand.best_hand <= 21 and dealer.hand.best_hand != 21:
        game.dealer.play_out_hand(game.deck)
        game.dealer.reveal_hand()
        game.player.show_hand()

        if game.dealer.hand.best_hand > 21:
            print("Dealer busts!, you win!")
            game.player.stack += game.pot * 2
        else:
            if game.player.hand.best_hand < game.dealer.hand.best_hand:
                print("You Lose")
            elif game.dealer.hand.best_hand < game.player.hand.best_hand:
                print("You Win!")
                game.player.stack += game.pot * 2
            elif game.dealer.hand.best_hand == game.player.hand.best_hand:
                print("Push!")
                game.player.stack += game.pot
    else:
        if dealer.hand.best_hand == 21:
            print("Dealer has blackjack! You lose!")
        else:
            print("Your hand is over 21, you lose!!")

    game_loop = game.play_again()
