from card import Card
from game_options import GameOptions
from game import Game
from hand import Hand


def test_create_hands():
    options = GameOptions()
    new_game = Game(options, "Alan")
    new_game.create_hands(10)

    assert len(new_game.player.hands[0].cards) == 2
    assert len(new_game.dealer.hand.cards) == 2
    assert len(new_game.deck.cards) == 48
    assert new_game.player.hands[0].bet == 10


def test_bust():
    options = GameOptions()
    new_game = Game(options, "Alan")
    hand = Hand(10, [Card("J", "hearts"), Card("Q", "diamonds")])
    assert not new_game.check_bust(hand)
    hand.cards.append(Card("K", "spades"))
    assert new_game.check_bust(hand)


def test_push():
    options = GameOptions()
    new_game = Game(options, "Alan")
    hand = Hand(10, [Card("J", "hearts"), Card("Q", "diamonds")])
    hand2 = Hand(10, [Card("K", "hearts"), Card("J", "diamonds")])
    assert new_game.check_push(hand, hand2)
    hand.cards.append(Card("A", "spades"))
    assert not new_game.check_push(hand, hand2)


def test_can_split_by_rank():
    options = GameOptions()
    options.split_by_rank = True
    new_game = Game(options, "Alan")
    hand = Hand(10, [Card("Q", "hearts"), Card("Q", "diamonds")])
    assert new_game.can_split(hand)
    hand = Hand(10, [Card("Q", "hearts"), Card("10", "diamonds")])
    assert not new_game.can_split(hand)


def test_can_split_by_value():
    options = GameOptions()
    options.split_by_rank = True
    new_game = Game(options, "Alan")
    hand = Hand(10, [Card("Q", "hearts"), Card("10", "diamonds")])
    assert not new_game.can_split(hand)


def test_can_double_normal():
    options = GameOptions()
    options.split_by_rank = True
    new_game = Game(options, "Alan")
    hand = Hand(10, [Card("6", "clubs"), Card("8", "hearts")])
    assert new_game.can_double(hand)
    hand.cards.append(Card("3", "diamonds"))
    assert not new_game.can_double(hand)

def test_can_double_9_10_11():
    options = GameOptions()
    options.double_9_10_11 = True
    new_game = Game(options, "Alan")
    hand = Hand(10, [Card("6", "clubs"), Card("3", "hearts")])
    assert new_game.can_double(hand)
    hand = Hand(10, [Card("6", "clubs"), Card("4", "hearts")])
    assert new_game.can_double(hand)
    hand = Hand(10, [Card("6", "clubs"), Card("5", "hearts")])
    assert new_game.can_double(hand)
    hand = Hand(10, [Card("6", "clubs"), Card("8", "hearts")])
    assert not new_game.can_double(hand)


def test_can_double_9_10():
    options = GameOptions()
    options.double_9_10 = True
    new_game = Game(options, "Alan")
    hand = Hand(10, [Card("6", "clubs"), Card("3", "hearts")])
    assert new_game.can_double(hand)
    hand = Hand(10, [Card("6", "clubs"), Card("4", "hearts")])
    assert new_game.can_double(hand)
    hand = Hand(10, [Card("6", "clubs"), Card("5", "hearts")])
    assert not new_game.can_double(hand)
    hand = Hand(10, [Card("6", "clubs"), Card("8", "hearts")])
    assert not new_game.can_double(hand)

def test_can_surrender():
    options = GameOptions()
    new_game = Game(options, "Alan")
    hand1 = Hand(10, [Card("6", "clubs"), Card("10", "hearts")])
    
