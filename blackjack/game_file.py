from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.player_hand import Player_hand
from blackjack.dealer_hand import Dealer_hand
from blackjack.user import User









# Account for a push occurring





def game_flow():
    fresh_deck = Deck()
    fresh_deck.shuffle_deck()
    player = User()
    print("You have {} chips.".format(player.chip_count))
    # Ask user if they'd like to deal or place a bet
        #Don't let them deal unless they've bet something


    # Initial deal to player
    new_cards = Player_hand([fresh_deck.deal_card(), fresh_deck.deal_card()])
    # Initial dealing to dealer (1 card for now only)
    dealer_cards = Dealer_hand([fresh_deck.deal_card()])

    #player hits, so they want this card
    next_card = Player_hand(fresh_deck.deal_card())
    #below adds the new card to player's list of cards
    new_cards.cards.append(next_card.cards)
    print(new_cards)
    print(dealer_cards)




def help():
    print("""Welcome to Cooper's Blackjack!
          The rules of the game are simple. They're listed below, but can
          be reached again if need be.

          Type 'quit' to exit the game at any time.
          Type 'help' to access this help menu again.
          Type 'hit' to receive another card.
          Type 'stay' to maintain your position and let the dealer go.
          Type 'bet' to change your bet from the previous round, or place
                    a bet for the first time.

    """)

if __name__ == '__main__':
    game_flow()
