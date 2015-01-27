from blackjack.dealer_hand import DealerHand
from blackjack.player_hand import PlayerHand
import sys


class GameManager:
    """Controls who wins and loses

    Responsibilities:

    * Look at results and decide winner or loser
    * Double user's bet if they win
    * If tie, then insert push rules

    Collaborators:

    * Send User bet
    * Initiate next game to User
    """

    def dealer_flipping(self, dealer_cards, card_deck, player, player_hand):
        """Manages the dealer's turn. Decides when the user is supposed to hit,
        stay, win, or lose.
        dealer_cards = the dealer's hand
        card_deck = the deck of cards you're playing with
        player = the user
        player_hand = the user's hand"""

        while True:
            self.hit_hand(dealer_cards, card_deck)
            dealer_cards.dealer_card_count(dealer_cards.cards)
            dealer_next_steps = dealer_cards.dealer_actions()
            print('The dealer now has', dealer_cards)

            if dealer_next_steps == 'stay':
                if dealer_cards.card_count > player_hand.count:
                    print("You lost\n", ("="*40))
                    if player.chip_count == 0:
                        print("You are out of chips! Goodbye.")
                        sys.exit()
                    return 'gameflow'

                elif dealer_cards.card_count == player_hand.count:
                    print("You tied the dealer. Your bet "
                          "will be refunded.")
                    player.chip_count += player.bet
                    return 'gameflow'
                else:
                    print("You Won!\n", ("="*40))
                    player.chip_count += (2 * player.bet)
                    return 'gameflow'
            elif dealer_next_steps == 'bust':
                print("You won! The dealer busted.", ("="*40))
                player.chip_count += (2 * player.bet)
                return 'gameflow'
            else:
                print("The dealer must hit.")

    def busted(self, player):
        if player.chip_count == 0:
            print("You are out of chips! Goodbye.")
            sys.exit()
        return "You busted."

    def twenty_one(self, player):
        player.chip_count += (2 * player.bet)
        return 'You won!'

    def hit_hand(self, persons_hand, deck):
        persons_hand.cards.extend([deck.deal_card()])
        return persons_hand

    def player_options(self, player, user_action, fresh_deck, player_hand,
                       dealer_cards):

        if user_action == 'double':
            player.bet_chips(player.bet)
            player.bet = player.bet * 2
            print('You have ', self.hit_hand(player_hand, fresh_deck))
            print('Dealer has ', self.hit_hand(dealer_cards, fresh_deck))
            self.dealer_flipping(dealer_cards, fresh_deck, player, player_hand)
            return 'over'

        elif user_action == 'hit':
            self.hit_hand(player_hand, fresh_deck)
            return 'hit'

        elif user_action == 'stay':
            over = self.dealer_flipping(dealer_cards, fresh_deck,
                                        player, player_hand)
            return over
