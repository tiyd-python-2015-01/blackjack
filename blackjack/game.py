from card import Card
from deck import Deck
from dealer_hand import Dealer_Hand
from player_hand import Player_Hand

deck = Deck()
player1 = Player_Hand()
dealer = Dealer_Hand()
chips = 100

while True:
    deck = Deck()
    deck.shuffle_deck()

    print("\nAll bets are 10 chips, you have {} chips left\n".format(chips))
    if chips < 10:
        print("All out of money, you lose")
        break
    if chips >= 10:
        print("Alright you have enough chips, you bet 10")
        chips -= 10

    player_draw2 = player1.draw_two(deck)
    dealer_draw2 = dealer.draw_two(deck)
    print("\nYou have a {} and a {}".format(player_draw2[0],
                                            player_draw2[1]))
    print("You are currently at {}".format(player1.hand_value()))
    if player1.hand_value() == 21:
        print("Blackjack!!! You Win!!!")
        chips += 20
    else:
        print("\n")
        print("The dealer is showing a {}\n".format(dealer_draw2[1]))

        response = input("Type 'hit' if you would like a hit or 'stand' if you "
                         "would like to stand\n\n")

        while True:
            """Handles user response and decisions"""
            print(len(player1.hand))
            # if player1.hand_value() == 21 and len(player1.hand) == 2:
            #     print("Blackjack!!! You Win!!!")
            #     break

            if response == "stand":
                print("\nNow its the dealers turn")
                break

            elif response == "hit":
                new_card = deck.draw()  # draws a card from deck and appends
                player1.hit(new_card)   # it to hand list using the hit fuction
                print("\nYou drew a {}".format(new_card))
                print("\nYou now have a {}".format(player_draw2[0:]))
                print("You are now at {}\n".format(player1.hand_value()))
                if player1.hand_value() > 21:
                    for card in player1.hand:
                        if card.rank == "Ace":
                            card.value = 1
                            print("\nYou now have a {}".format(player_draw2[0:]))
                            print("You are now at {}\n".format(player1.hand_value()))
                            break
                if player1.hand_value() > 21:
                    print("Bust, sorry the dealer wins this hand\n")
                    break
                response = input("Type 'hit' if you would like a hit or 'stand'"
                                 "if you would like to stand\n")

            else:
                print("Please type 'hit' or 'stand'")
                break

        while player1.hand_value() < 22:
            """Handles dealer(computer) response and decisions"""

            print("The dealer is showing a {}\n".format(dealer_draw2[1:]))

            if dealer.hand_value() > 21:
                break
            elif dealer.hand_value() < 21 and dealer.hand_value() >= 17:
                print("The dealer will stand with a {}".format
                      (dealer.hand_value()))
                break
            elif dealer.hand_value() < 17:
                new_card = deck.draw()
                dealer.hit(new_card)
                new_hand_value = dealer.hand_value()
                print("The dealer drew a {}".format(new_card))
                if new_hand_value > 21:
                    break
            else:
                print("The dealer will stay\n")
                print("The dealer reveals a value of {}".format
                      (dealer.hand_value()))
                break

        if dealer.hand_value() <= 21 and dealer.hand_value() > player1.hand_value():
            print("Sorry, the dealer had a higher value.\nYou lose\n")

        if dealer.hand_value() <= 21 and dealer.hand_value() < player1.hand_value() and player1.hand_value() <= 21:
            print("You Win!!!")
            chips += 20

        if dealer.hand_value() > 21:
            print("You Win!!!")
            chips += 20

        if dealer.hand_value() == player1.hand_value():
            print("It's a Push, lets pretend this never happened")
            chips += 10
