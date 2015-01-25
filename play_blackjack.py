from card import Card, ranks, suits
from deck import Deck
from player import Player
from hand import Hand
from game_state import Game
import sys


def intro():
    print("="*80)
    print('\n____  __           __          __           __'
          '\n/ __ )/ /___ ______/ /__       / /___ ______/ /__'
          '\n/ __  / / __ `/ ___/ //_/  __  / / __ `/ ___/ //_/'
          '\n/ /_/ / / /_/ / /__/ ,<    / /_/ / /_/ / /__/ ,<'
          '\n/_____/_/\__,_/\___/_/|_|   \____/\__,_/\___/_/|_|'
          )
    print("\n\n")
    print("="*80)


def get_shoe_size():
    """Allows the player to choose 1 or 6 decks for the shoe."""
    while True:
        try:
            shoe_size = int(input("\nPlay with 1 or 6 decks in the shoe?\n>:"))
            if shoe_size == 1 or shoe_size == 6:
                break
            else:
                print("\nLooking for a 1 or a 6...try again.")
                continue
        except ValueError:
            print("\nLooking for a 1 or a 6...try again.")
            continue
    return shoe_size


def display():
    """Prints out the current hands as well as the player's bet/bank."""
    print('*' * 80)
    print('Dealer Hand:{} and Hole:??'.format([str(card)
                                               for card
                                               in game.dealer_hand.cards[1:]]))
    print('*' * 80)
    print('Your Hand:{}'.format([str(card)
                                 for card
                                 in game.player_hand.cards]))
    print("Bank: {}, Bet: {}".format(player.bank, 10))
    print('*' * 80)


def player_move():
    move = input("(H)it or (S)tand? \n>:").lower()
    if move == 'h':
        game.hit()
        return
    elif move == 's':
        return 'STAND'
    else:
        print("I'm sorry what was that?")
        return player_move()


def dealer_move():
    """Contains the dealers simple logic."""
    dealer_value = game.dealer_hand.get_value()
    if len(game.dealer_hand.cards) == 2 and dealer_value == 17:
        print("\nDealer hits...")
        game.dealer_hit()
        return 'HIT'
    elif game.dealer_hand.value < 17:
        print("\nDealer hits...")
        game.dealer_hit()
        return 'HIT'
    else:
        return 'STAND'


def game_flow():
    """Contains the turn scheme of the game. Including hand evaluations."""
    print("\nSetting up a new game...")
    game.deal()
    print("\nDealing the cards...")
    print("\n\nLet's begin!!!")
    while True:
        display()
        pmove = player_move()
        dmove = dealer_move()
        player_value = game.player_hand.get_value()
        if player_value > 21:
            return
        elif pmove == 'STAND' and dmove == 'STAND':
            return


def results():
    """Prints the final hand values and determines the winner of the game."""
    player_value = game.player_hand.get_value()
    dealer_value = game.dealer_hand.get_value()
    print("Your hand: {}, Value: {}".format([str(card)
                                            for card
                                            in game.player_hand.cards],
                                            player_value))
    print("Dealer's hand: {}, Value: {}".format([str(card)
                                                for card
                                                in game.dealer_hand.cards],
                                                dealer_value))
    if player_value == 'BLACKJACK' and dealer_value != 'BLACKJACK':
        print("\nWhoa you got BLACKJACK!!")
        player.win_blackjack(bet)
        return
    elif player_value > 21:
        print("Oh no! You BUSTED!!")
        return 'BUST'
    elif player_value == 21 and dealer_value == 'BLACKJACK':
        print("\nOh no! the house got BLACKJACK!!")
        return
    elif dealer_value > 21:
        print("\nThe house busts! You win!")
        player.win_no_blackjack(bet)
        return
    elif player_value > dealer_value:
        print("\nYou beat the house!!")
        player.win_no_blackjack(bet)
        return
    elif player_value < dealer_value:
        print("\nOh no! The house wins!")
        return
    elif player_value == dealer_value:
        print("\nAhh it's a push...")
        player.push(bet)
    else:
        return


def get_bet():
    """Allows the player to choose their bet."""
    while True:
        try:
            bet = int(input("\nHow much will you bet on this hand?\n>:"))
            break
        except ValueError:
            print("\nThat was not a valid bet. Try again...")
    return bet


if __name__ == "__main__":
    intro()
    player = Player()
    shoe_size = get_shoe_size()
    while player.bank > 0:
        game = Game()
        game.shoe.set(shoe_size)
        print("\nYou have ${}".format(player.bank))
        bet = get_bet()
        player.bet(bet)
        print("\nTaking your bet...")
        game_flow()
        results()
    print("\n\nGet outta here!! You're broke!!")
    sys.exit()
