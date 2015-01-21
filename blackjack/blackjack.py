from class_card import Card
from class_deck import Deck
from class_player_hand import Player_hand
from class_dealer_hand import Dealer_hand



dealt_cards, live_deck = Deck.deal_cards(2, Deck.shuffle_deck(), 2)

Player_hand.cards.append(dealt_cards[0])
Player_hand.cards.append(dealt_cards[1])
Dealer_hand.cards.append(dealt_cards[2])
Dealer_hand.cards.append(dealt_cards[3])

# dealcards(2)
    # user gets 2 and dealer gets 2.
    # dealer gets 1 that is face down


print(Player_hand.cards)
print(Dealer_hand.cards)
