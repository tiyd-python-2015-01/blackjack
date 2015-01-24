from blackjack.player import Player
from blackjack.player import Dealer
from blackjack.carddeckshoe import Card
from blackjack.interface import Interface

def test_create_interface():
    pass

# def test_display_hands():
#     player = Player()
#     dealer = Dealer()
#     player.get_hand([Card("King", "♢"), Card("Queen", "♤")])
#     dealer.get_hand([Card("One", "♢"), Card("Ten", "♧")])
#     interface = Interface()
#     printout = "Your hand:\nKing of ♢\nQueen of ♤\n\nDealer hand:\nTen of ♧\n"
#     print(interface.display_hands(player,dealer))
#     assert interface.display_hands(player,dealer) == printout
