from blackjack.player import Player
from blackjack.player import Dealer
from blackjack.carddeckshoe import Card
from blackjack.interface import Interface

def test_create_interface():
    pass

def test_display_hands():
    player = Player()
    dealer = Dealer()
    player.get_hand([Card("King", "Diamonds"), Card("Queen", "Spades")])
    dealer.get_hand([Card("One", "Diamonds"), Card("Ten", "Clubs")])
    interface = Interface()
    printout = "Your hand is King of Diamonds and Queen of Spades\nDealer is showing One of Diamonds"
    print(interface.display_hands(player,dealer))
    assert interface.display_hands(player,dealer) == printout
