from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.player_hand import Player_hand
from blackjack.dealer_hand import Dealer_hand


fresh_deck = Deck()
fresh_deck.shuffle_deck()

new_cards = Player_hand([fresh_deck.deal_card(), fresh_deck.deal_card()])
print(new_cards)

next_card = Player_hand(fresh_deck.deal_card())
print(next_card)

new_cards.cards.append(next_card.cards)
print(new_cards)

print(new_cards.player_card_count(new_cards.cards))



# dealcards(2)
    # user gets 2 and dealer gets 2.
    # dealer gets 1 that is face down
