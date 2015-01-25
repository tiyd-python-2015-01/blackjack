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

    print("\n \n")
    print("Let's play blackjack!")

    play_game = True
    while play_game:

        p_win = False
        d_win = False
        tie = False
        p_bust = False
        d_bust = False
        p_blackjack = False
        d_blackjack = False

        while not (p_win or d_win or tie or p_blackjack or d_blackjack):
            game = Game()
            deck = game.create_and_shuffle_deck()
            player_hand = Hand()
            dealer_hand = Hand()

            print("\n \n")
            print("New Hand\n")

            while True:
                print("You have {} chips.".format(player.chips))
                print("What is your bet?")
                new_bet = input("> ")
                player.bet = int(new_bet)
                if player.bet <= player.chips:
                    break

            player.make_bet()

            player_hand.get_card(deck)
            dealer_hand.get_card(deck)
            player_hand.get_card(deck)
            dealer_hand.get_card(deck)

            player_hand.value = player_hand.valuation()
            dealer_hand.value = dealer_hand.valuation()

            print("Player hand: {} {}".format(
                player_hand.value, player_hand.cards))
            print("Dealer shows: {} [{}]".format(
                dealer.shown_value(dealer_hand), dealer.shown(dealer_hand)))
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
                    print("")
                    print("{}".format(player_hand.new_card()))
                    print("")
                    print("Player has: {} {}".format(
                        player_hand.value, player_hand.cards))
                    print("Dealer shows: {} [{}]".format(
                        dealer.shown_value(dealer_hand), dealer.shown(
                            dealer_hand)))
                    print("")
                    p_bust = game.bust_check(player_hand)
                    if p_bust is True:
                        break
                    hit_or_stand = 0
            if p_bust is True:
                break

            print("")
            print("Dealer's turn.")
            input("Press ENTER to continue. \n")
            print("Dealer shows his hole card.")
            print("Dealer has: {} {}".format(
                dealer_hand.value, dealer_hand.cards))
            input("Press ENTER to continue. \n")
            print("")

            d_blackjack = game.blackjack_check(dealer_hand)
            if d_blackjack is True:
                break

            hit_or_stand = dealer.hit_test(dealer_hand)
            while hit_or_stand == "HIT":
                print("Dealer hits. \n")
                dealer_hand.get_card(deck)
                dealer_hand.value = dealer_hand.valuation()
                print("{}".format(dealer_hand.new_card()))
                print("")
                print("Player has: {} {}".format(
                    player_hand.value, player_hand.cards))
                print("Dealer has: {} {}".format(
                    dealer_hand.value, dealer_hand.cards))
                input("Press ENTER to continue. \n")
                d_bust = game.bust_check(dealer_hand)
                if d_bust is True:
                    break
                hit_or_stand = dealer.hit_test(dealer_hand)
            if d_bust is True:
                break

            print("Dealer stands.")
            input("Press ENTER to continue. \n")
            print("Player has: {} {}".format(
                player_hand.value, player_hand.cards))
            print("Dealer has: {} {}".format(
                dealer_hand.value, dealer_hand.cards))

            higher_hand = game.higher_hand(player_hand, dealer_hand)
            if higher_hand == 'p_hand':
                p_win = True
            if higher_hand == 'd_hand':
                d_win = True
            else:
                tie = True

        if p_blackjack and d_blackjack:
            print("Wow. Crap. The dealer also had blackjack.")
            print("That's a push.")
            player.push()
            print("You have {} chips remaining.".format(player.chips))
        else:
            if p_blackjack:
                print("You've got blackjack!  You win.")
                player.win_blackjack()
                print("You have {} chips remaining.".format(player.chips))
            if d_blackjack:
                print("Dealer has blackjack.  Dealer wins.")
                print("You have {} chips remaining.".format(player.chips))
            elif p_bust:
                print("Sorry, you busted!  Dealer wins.")
                print("You have {} chips remaining.".format(player.chips))
            elif d_bust:
                print("Dealer busts!  You win.")
                player.win_bet()
                print("You have {} chips remaining.".format(player.chips))
            elif p_win:
                print("You have the higher hand!  You win.")
                player.win_bet()
                print("You have {} chips remaining.".format(player.chips))
            elif d_win:
                print("Dealer has the higher hand!  Dealer wins.")
                print("You have {} chips remaining.".format(player.chips))
            elif tie:
                print("That's a push.")
                player.push()
                print("You have {} chips remaining.".format(player.chips))

        if player.chips <= 0:
            print("You're out of chips!  You're done!  Go home!")
            print("I hope you learned a valuable lesson about gambling.")
            exit()

        print("")

        checker = 1
        while checker == 1:
            answer = (input("Play again?  Y/N: ")).upper()
            if answer == "Y":
                checker = 0
            if answer == "N":
                checker = 0
                play_game = False
