from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.player import Player
from blackjack.dealer import Dealer
from blackjack.game import Game

import blackjack.functions as fun

if __name__ == "__main__":

    player = Player()
    dealer = Dealer()

    p_win = False
    d_win = False
    tie = False
    p_bust = False
    d_bust = False
    p_blackjack = False
    d_blackjack = False

    while not (p_win or d_win or p_bust or d_bust or p_blackjack or d_blackjack):
        game = Game()
        deck = game.create_and_shuffle_deck()
        player_hand = Hand()
        dealer_hand = Hand()


        player_hand.get_card(deck)
        dealer_hand.get_card(deck)
        player_hand.get_card(deck)
        dealer_hand.get_card(deck)

        player_hand.value = player_hand.valuation()
        dealer_hand.value = dealer_hand.valuation()

        print("Player hand: {}".format(player_hand.cards))
        print("Dealer shows: {}".format(dealer.shown(dealer_hand)))
        print(player_hand.value)
        print(dealer_hand.value)
        p_blackjack = game.blackjack_check(player_hand)
        d_blackjack = game.blackjack_check(dealer_hand)
        if p_blackjack is True:
            break



        hit_or_stand = 0
        while not fun.hit_stand(hit_or_stand):
            hit_or_stand = (input("Hit or Stand? ")).upper()

            if hit_or_stand == "HIT":
                player_hand.get_card(deck)
                player_hand.value = player_hand.valuation()
                print("Player hand: {}".format(player_hand.cards))
                print("Dealer hand: {}".format(dealer.shown(dealer_hand)))
                p_bust = game.bust_check(player_hand)
                if p_bust == True:
                    break
                hit_or_stand = 0
        if p_bust == True:
            break

        print("Dealer's turn.")
        print("Dealer has: {}".format(dealer_hand.cards))
        #d_blackjack = game.blackjack_check()

        hit_or_stand = dealer.hit_test(dealer_hand)
        while hit_or_stand == "HIT":
            print("Dealer hits.")
            dealer_hand.get_card(deck)
            dealer_hand.value = dealer_hand.valuation()
            print("Dealer hand: {}".format(dealer_hand.cards))
            d_bust = game.bust_check(dealer_hand)
            if d_bust == True:
                break
            hit_or_stand = dealer.hit_test(dealer_hand)
        if d_bust == True:
            break

        print("Dealer stands.")
        higher_hand = game.higher_hand(player_hand, dealer_hand)
        if higher_hand == p_hand:
            p_win = True
        if higher_hand == d_hand:
            d_win = True
        else:
            tie = True



    if p_blackjack and d_blackjack:
        #TIE GAME Conditions
    else:
        if p_blackjack:
            #Player blackjack!
            #deal out the appropriate chips
        if d_blackjack:
            #dealer has blackjack
        if p_bust:
            print("Sorry, you busted!  Dealer wins.")
            print("You have {} chips remaining.".format(player.chips))
        if d_bust:
            print("Dealer busts!  You win.")
            player.win_bet
            print("You have {} chips remaining.".format(player.chips))
