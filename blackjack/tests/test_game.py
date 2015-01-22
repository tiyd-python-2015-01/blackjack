from card import Card
from game_options import GameOptions
from game import Game
from hand import Hand


def test_create_hands():
    options = GameOptions()
    new_game = Game(options, "Alan")
    new_game.create_hands()

    assert len(new_game.player.hands[0].cards) == 2
    assert len(new_game.dealer.hand.cards) == 2
    assert len(new_game.deck.cards) == 48

def test_bust():
    options = GameOptions()
    new_game = Game(options, "Alan")
    hand = Hand([Card("J", "hearts"), Card("Q", "diamonds")])
    assert not new_game.check_bust(hand)
    hand.cards.append(Card("K", "spades"))
    assert new_game.check_bust(hand)

def test_push():
    options = GameOptions()
    new_game = Game(options, "Alan")
    hand = Hand([Card("J", "hearts"), Card("Q", "diamonds")])
    hand2 = Hand([Card("K", "hearts"), Card("J", "diamonds")])
    assert new_game.check_push(hand, hand2)
    hand.cards.append(Card("A", "spades"))
    assert not new_game.check_push(hand, hand2)

def test_can_split_by_rank():
    options = GameOptions()
    options.split_by_rank = True
    new_game = Game(options, "Alan")
    hand = Hand([Card("Q", "hearts"), Card("Q", "diamonds")])
    assert new_game.can_split(hand)
    hand = Hand([Card("Q", "hearts"), Card("10", "diamonds")])
    assert not new_game.can_split(hand)

def test_can_split_by_value():
    options = GameOptions()
    options.split_by_rank = True
    new_game = Game(options, "Alan")
    hand = Hand([Card("Q", "hearts"), Card("10", "diamonds")])
    assert not new_game.can_split(hand)
