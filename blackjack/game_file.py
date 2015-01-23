from blackjack.card import Card
from blackjack.dealer_hand import DealerHand
from blackjack.deck import Deck
from blackjack.player_hand import PlayerHand
from blackjack.user import User
from blackjack.game_manager import GameManager
import sys


def run_game_func():
    game_flow(game_setup())

def game_setup():
    player = User()
    game_help()
    print("You have {} chips.\n".format(player.chip_count))


    return player

def game_flow(player):
    fresh_deck = Deck()
    fresh_deck.shuffle_deck()

    user_pregame_steps(player.user_pregame_input(), player)

    print("Let's deal the hand now.\n")

    # Initial deal to player
    new_cards = PlayerHand([fresh_deck.deal_card(), fresh_deck.deal_card()])
    new_cards.player_card_count(new_cards.cards)
    print('Player has {} --A total of {}'.format(new_cards, new_cards.count))

    # Initial dealing to dealer (1 card for now only)
    dealer_cards = DealerHand([fresh_deck.deal_card()])
    print('Dealer has {} and an unknown card\n'.format(dealer_cards))

    while True:
        # Ask user what they wants to do
        new_cards.player_card_count(new_cards.cards)
        user_next_stage = new_cards.player_actions()

        if user_next_stage == 'bust':
            print("You lost\n", ("="*40))
            game_flow(player)

        elif user_next_stage == '21':
            print("You won")
            player.chip_count += (2 * player.bet)
            game_flow(player)

        elif user_next_stage == 'choice':
            user_action = user_in_game_steps(player.user_in_game_input(),
                                             player)
            if user_action == 'hit':
                next_card = PlayerHand(fresh_deck.deal_card())
                new_cards.cards.append(next_card.cards)
                print('\nYou now have - ', new_cards.cards)

            elif user_action == 'stay':
                dealer_next_card = DealerHand([fresh_deck.deal_card()])
                dealer_cards.cards.extend(dealer_next_card.cards)

                print("You've elected to stay. The dealer flipped their"
                      " second card and it was a {}. The dealer now has"
                      ":\n{}".format(dealer_next_card, dealer_cards))
                gm = GameManager()
                response = gm.dealer_flipping(dealer_cards,
                                              fresh_deck,
                                              player,
                                              new_cards)
                if response == 'gameflow':
                    game_flow(player)



# Account for a push occurring


def game_help():
    print("""Welcome to Cooper's Blackjack!
          The rules of the game are simple. They're listed below, but can
          be reached again if need be.

          Type 'quit' to exit the game at any time.
          Type 'help' to access this help menu again.
          Type 'chips' to see how many chips you have remaining.\n""")

def user_pregame_steps(user_input, player):
    if user_input == 'help':
        game_help()
        player.user_pregame_input()
        return 'game_help()'

    elif user_input == 'quit':
        sys.exit()
        return 'sys.exit()'

    elif user_input == 'chips':
        print(player.chip_count)
        player.user_pregame_input()
        return 'chips'

    elif type(user_input) == int:
        print(("="*40) , "\nYou've bet {} chips "
               "on this hand.".format(user_input))
        player.bet_chips(user_input)
        return user_input

    else:
        print("That is not a valid entry.")
        player.user_pregame_input()
        return 'player.user_pregame_input()'

def user_in_game_steps(user_input, player):
    if user_input == 'help':
        game_help()
        player.user_in_game_input()
        return 'game_help()'

    elif user_input == 'quit':
        sys.exit()
        return 'sys.exit()'

    elif user_input == 'chips':
        print(player.chip_count)
        player.user_in_game_input()
        return 'chips'

    elif user_input == 'hit':
        # Add in 'hit' functionality
        return 'hit'
    elif user_input == 'stay':
        # Add in 'stay' functionality
        return 'stay'


if __name__ == '__main__':
    run_game_func()
