from blackjack.functions import*
from blackjack.card import Card
from blackjack.hand import Hand
from blackjack.player import Player
from blackjack.dealer import Dealer
from blackjack.deck import Deck


player_one = Player()

dealer_one = Dealer()

deck_one = Deck()

over_hand = Hand()
over_hand.add(Card("Queen", "Spades"))
over_hand.add(Card("10", "Clubs"))
over_hand.add(Card("Queen", "Clubs"))

under_hand = Hand()
under_hand.add(Card("Jack", "Hearts"))
under_hand.add(Card("7", "Diamonds"))

blackjack_hand = Hand()
blackjack_hand.add(Card("Jack", "Spades"))
blackjack_hand.add(Card("Ace", "Clubs"))


def test_check_bust():
    assert check_bust(over_hand) == True
    assert check_bust(under_hand) == False
    assert check_bust(blackjack_hand) == False

def test_blackjack_check():
    assert blkjck_chk(over_hand) == False
    assert blkjck_chk(blackjack_hand) == True

def test_hit():
    hit(player_one, deck_one)
    assert(len(player_one.hand)) == 1
    hit(dealer_one, deck_one)
    assert(len(dealer_one.hand)) == 1
