from dealer import Dealer
from player import Player
from game import Game
from hand import Hand
from card import Card
from shoe import Shoe, Diamonds, Spades


dealer = Dealer()
player = Player("John")
shoe = Shoe(6)
game = Game(dealer, player, shoe)


def test_new_turn():
    game.new_turn()
    assert game.pot == 0
    assert len(shoe) == 308
    assert player.stack == 100
    assert len(player.hand.hand) == 2
    assert len(dealer.hand.hand) == 2


def test_place_bet():
    game.place_bet(5)
    assert player.stack == 95
    assert game.pot == 5


def test_insurance():
    dealer = Dealer()
    player = Player("John")
    shoe = Shoe(6)
    game = Game(dealer, player, shoe)
    game.place_bet(10)
    game.insurance(5, 10)
    assert player.stack == 85
    assert game.insurance(6, 10) == "more than half"


def test_dealer_blackjack_with_insurance():
    dealer2 = Dealer(Hand([Card('J', Diamonds), Card('A', Spades)]))
    player = Player("John")
    shoe = Shoe(6)
    game = Game(dealer2, player, shoe)
    game.place_bet(10)
    game.insurance(5, 10)
    assert game.player.stack == 100
    print(game.pot)


def test_dealer_has_21():
    dealer1 = Dealer(Hand([Card('J', Diamonds), Card('A', Spades)]))
    game1 = Game(dealer1, player, shoe)
    assert game1.dealer_has_blackjack() is True
    dealer2 = Dealer(Hand([Card(10, Diamonds), Card('A', Spades)]))
    game2 = Game(dealer2, player, shoe)
    assert game2.dealer_has_blackjack() is True
    dealer3 = Dealer(Hand([Card(10, Diamonds), Card('J', Spades)]))
    game3 = Game(dealer3, player, shoe)
    assert game3.dealer_has_blackjack() is False


def test_player_has_21():
    player1 = Player("John",
                     hand=Hand([Card('J', Diamonds), Card('A', Spades)]))
    game1 = Game(dealer, player1, shoe)
    assert game1.player_has_blackjack() is True
    player2 = Player("Jill",
                     hand=Hand([Card(10, Diamonds), Card('A', Spades)]))
    game2 = Game(dealer, player2, shoe)
    assert game2.player_has_blackjack() is True
    player3 = Player("Sam",
                     hand=Hand([Card(10, Diamonds), Card('J', Spades)]))
    game3 = Game(dealer, player3, shoe)
    assert game3.player_has_blackjack() is False
