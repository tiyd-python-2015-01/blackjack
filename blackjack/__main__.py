from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.player import Player
from blackjack.dealer import Dealer
from blackjack.game import Game


if __name__ == "__main__":

    player = Player()
    dealer = Dealer()

#    while True:
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
    print("Dealer hand: {}".format(dealer.shown(dealer_hand)))
    print(player_hand.value)
    print(dealer_hand.value)


    hit_or_stand = (input("Hit or Stand? ")).upper()
    while hit_or_stand == "HIT":
        player_hand.get_card(deck)
        player_hand.value = player_hand.valuation()
        print("Player hand: {}".format(player_hand.cards))
        print("Dealer hand: {}".format(dealer.shown(dealer_hand)))
        hit_or_stand = (input("Hit or Stand? ")).upper()
