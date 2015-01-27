from blackjack.card import Card
from blackjack.dealer_hand import DealerHand
from blackjack.deck import Deck
from blackjack.player_hand import PlayerHand
from blackjack.user import User
from blackjack.game_manager import GameManager
import sys


def run_game_func():
    """Master function to run the entire game. Setup and all"""

    game_flow(game_setup())


def game_setup():
    """Pre-dealing of blackjack. This function manages the setup of the user,
    giving them 100 chips to start with, and displays the help."""

    player = User()
    player.chip_count = 100
    game_help()
    print("You have {} chips.\n".format(player.chip_count))
    return player


def game_flow(player):
    """Function manages the actual flow of card game itself. Dealing,
    hitting, etc. """

    gm = GameManager()
    fresh_deck = Deck()
    fresh_deck.shuffle_deck()

    user_pregame_steps(player.user_pregame_input(), player)

    print("Let's deal the hand now.\n")

    player_cards = PlayerHand([fresh_deck.deal_card(), fresh_deck.deal_card()])
    player_cards.player_card_count(player_cards.cards)
    print('Player has {} --A total of {}'.format(player_cards,
                                                 player_cards.count))

    dealer_cards = DealerHand([fresh_deck.deal_card()])
    print('Dealer has {} and an unknown card\n'.format(dealer_cards))

    while True:
        print(player_cards)
        player_cards.player_card_count(player_cards.cards)
        user_next_stage = player_cards.player_actions()

        if user_next_stage == 'help':
            game_help()
        elif user_next_stage == 'quit':
            sys.exit()
        elif user_next_stage == 'chips':
            print(player.chip_count)
        elif user_next_stage == 'bust':
            print(gm.busted(player), '\n', ("="*40))
            game_flow(player)
        elif user_next_stage == '21':
            print(gm.twenty_one(player), ' You got 21!')
            game_flow(player)
        elif user_next_stage == 'choice':
            user_action = player.user_in_game_input()
            result = gm.player_options(player, user_action, fresh_deck,
                                       player_cards, dealer_cards)
            if result == 'gameflow':
                game_flow(player)


def game_help():
    """Simply displays the help for the game"""

    print("""Welcome to Cooper's Blackjack!
          The rules of the game are simple. They're listed below, but can
          be reached again if need be.

          Type 'quit' to exit the game at any time.
          Type 'help' to access this help menu again.
          Type 'chips' to see how many chips you have remaining.\n""")


def user_pregame_steps(user_input, player):
    """Function's use is to determine next steps based on the user_pregame_input
    function that is laid out in the users class.
    user_input = result of aforementioned function
    player = the specified player. Referring to the user class"""

    if user_input == 'help':
        game_help()
        user_pregame_steps(player.user_pregame_input(), player)
        return 'game_help()'

    elif user_input == 'quit':
        sys.exit()
        return 'sys.exit()'

    elif user_input == 'chips':
        print(player.chip_count)
        user_pregame_steps(player.user_pregame_input(), player)
        return 'chips'

    elif type(user_input) == int:
        print(("="*40), "\nYou've bet {} chips "
              "on this hand.".format(user_input))
        player.bet_chips(user_input)
        return user_input

    else:
        print("That is not a valid entry.")
        player.user_pregame_input()
        return 'player.user_pregame_input()'


if __name__ == '__main__':
    run_game_func()
