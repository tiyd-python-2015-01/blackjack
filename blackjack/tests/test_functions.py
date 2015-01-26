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
    assert check_bust(over_hand) is True
    assert check_bust(under_hand) is False
    assert check_bust(blackjack_hand) is False


def test_blackjack_check():
    assert blkjck_chk(over_hand) is False
    assert blkjck_chk(blackjack_hand) is True
