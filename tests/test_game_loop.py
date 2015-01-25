from card import Card
from deck import Deck
from pot import Pot
from player import Player
from player import Dealer
from game_loop import win_game
from game_loop import lose_game
from game_loop import game_logic



def test_win_game():
    """Test fn adds bet money to purse"""
    pot = Pot(100)
    pot.bet = 100
    win_game(pot)
    assert pot.purse == 200

def test_lose_game():
    """Test fn subtracts money from pot"""
    pot = Pot(100)
    pot.bet = 10
    lose_game(pot)

    assert pot.purse == 90

def test_game_logic_dealer_get_cards():
    """Test the dealer hits if < 17"""
    pot = Pot(100)
    pot.bet = 10
    deck = Deck()
    player = Player(deck)
    dealer = Dealer(deck)

    game_logic(dealer,player,pot)

    assert len(dealer) > 0

    dealer.hand = [Card("10","Clubs"), Card("3","Hearts"),
                    Card("2", "Diamonds")]

    game_logic(dealer,player,pot)

    assert len(dealer) > 3


def test_game_logic_losing():
    """Test losing conditions cause a lost bet"""
    pot = Pot(100)
    pot.bet = 10
    deck = Deck()
    player = Player(deck)
    dealer = Dealer(deck)
    player.hand = [Card("King", "Clubs"), Card("King", "Hearts"),
                   Card("King", "Diamonds")]
    dealer.hand = [Card("3", "Clubs"), Card("10", "Hearts"),
                   Card("7", "Diamonds")]

    game_logic(dealer,player,pot)

    assert pot.purse == 90

    player.hand = [Card("2","Clubs"), Card("10","Hearts"),
                   Card("3", "Diamonds")]

    dealer.hand = [Card("3","Clubs"), Card("10","Hearts"),
                   Card("7", "Diamonds")]
    game_logic(dealer,player, pot)

    assert pot.purse == 80

def test_game_logic_winning():
    """Test losing conditions cause a lost bet"""
    pot = Pot(100)
    pot.bet = 10
    deck = Deck()
    player = Player(deck)
    dealer = Dealer(deck)

    player.hand = [Card("9","Clubs"), Card("10","Hearts"),
                   Card("2", "Diamonds")]
    dealer.hand = [Card("9","Clubs"), Card("9","Hearts"),
                   Card("2", "Diamonds")]

    game_logic(dealer, player, pot)

    assert pot.purse == 110

    player.hand = [Card("King","Clubs"), Card("King","Hearts")]
    dealer.hand = [Card("9","Clubs"), Card("9","Hearts"),
                   Card("5", "Diamonds")]

    game_logic(dealer,player,pot)

    assert pot.purse == 120

def test_game_logic_tie():
    """Test hands of equal value result in a tie and no winning bet"""
    pot = Pot(100)
    pot.bet = 10
    deck = Deck()
    player = Player(deck)
    dealer = Dealer(deck)

    player.hand = [Card("King","Clubs"), Card("King","Hearts")]
    dealer.hand = [Card("King","Clubs"), Card("King","Hearts")]

    game_logic(dealer,player,pot)

    assert pot.purse == 100

    player.hand = [Card("King","Clubs"), Card("8","Hearts")]
    dealer.hand = [Card("9","Clubs"), Card("9","Hearts")]

    game_logic(dealer,player,pot)

    assert pot.purse == 100
