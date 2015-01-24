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
    assert new_game.player.money == 90


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


def test_can_split_resplitting():
    options = GameOptions()
    new_game = Game(options, "Alan")
    hand = Hand(10, [Card("J", "hearts"), Card("Q", "diamonds")])
    new_game.player.hands.append(hand)
    assert new_game.can_split(hand)
    new_game.player.hands.append(hand)
    assert new_game.can_split(hand)
    new_game.options.resplitting = False
    assert not new_game.can_split(hand)
    new_game.player.hands.pop()
    assert new_game.can_split(hand)


def test_resplitting_aces():
    options = GameOptions()
    new_game = Game(options, "Alan")
    hand = Hand(10, [Card("A", "hearts"), Card("A", "diamonds")])
    new_game.player.hands.append(hand)
    assert new_game.can_split(hand)
    new_game.player.hands.append(hand)
    print(len(new_game.player.hands))
    assert not new_game.can_split(hand)
    new_game.options.resplit_aces = True
    assert new_game.can_split(hand)


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
    new_game = Game(options, "Alan")
    hand = Hand(10, [Card("Q", "hearts"), Card("10", "diamonds")])
    assert new_game.can_split(hand)


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
    hand2 = Hand(10, [Card("7", "hearts"), Card("A", "spades")])
    assert new_game.can_surrender(hand1, hand2.cards[1])
    assert not new_game.can_surrender(hand1, hand2.cards[0])
    new_game.options.no_surrender = True
    assert not new_game.can_surrender(hand1, hand2.cards[1])
    assert not new_game.can_surrender(hand1, hand2.cards[0])


def test_hit_split_aces():
    options = GameOptions()
    new_game = Game(options, "Alan")
    hand1 = Hand(10, [Card("A", "spades"), Card("6", "hearts")])
    hand2 = Hand(10, [Card("A", "hearts"), Card("7", "spades")])
    new_game.player.hands.append(hand1)
    new_game.player.hands.append(hand2)
    assert not new_game.can_hit(hand1)
    new_game.player.hands.pop()
    assert new_game.can_hit(hand1)


def test_no_double_after_split():
    options = GameOptions()
    new_game = Game(options, "Alan")
    hand1 = Hand(10, [Card("A", "spades"), Card("6", "hearts")])
    hand2 = Hand(10, [Card("A", "hearts"), Card("7", "spades")])
    new_game.player.hands.append(hand1)
    new_game.player.hands.append(hand2)
    assert new_game.can_double(hand1)
    new_game.options.no_double_after_split = True
    assert not new_game.can_double(hand1)


def test_hit():
    options = GameOptions()
    new_game = Game(options, "Alan")
    hand = Hand(10, [Card("A", "spades"), Card("6", "hearts")])
    new_game.player.takes_hit(hand, new_game.deck.deal())
    assert len(hand.cards) == 3


def test_split():
    options = GameOptions()
    new_game = Game(options, "Alan")
    hand = Hand(10, [Card("J", "spades"), Card("J", "clubs")])
    new_game.player.hands.append(hand)
    new_game.player.splits(hand, [new_game.deck.deal(), new_game.deck.deal()])
    assert len(new_game.player.hands) == 2
    assert len(hand.cards) == 2
    assert hand.cards[0].rank == "J"
    assert new_game.player.hands[1].cards[0].rank == "J"
    assert len(new_game.player.hands[1].cards) == 2

def test_double_down():
    options = GameOptions()
    new_game = Game(options, "Alan")
    hand = Hand(10,[Card("2", "spades"), Card("J", "clubs")])
    new_game.player.doubles(hand, new_game.deck.deal())
    assert len(hand.cards) == 3
    assert hand.bet == 20
    assert new_game.player.money == 90

def test_surrender():
    options = GameOptions()
    new_game = Game(options, "Alan")
    hand = Hand(10,[Card("2", "spades"), Card("J", "clubs")])
    new_game.player.surrenders(hand)

def test_payout():
    options = GameOptions()
    new_game = Game(options, "Alan")
    new_game.create_hands(10)
    new_game.player.hands[0] = Hand(10,[Card("2", "spades"),
                                    Card("J", "clubs")])
    new_game.dealer.hand = Hand(10,[Card("3", "spades"),
                                    Card("Q", "clubs")])
    new_game.payout(new_game.player.hands[0], new_game.dealer.hand)
    assert new_game.player.money == 110

    new_game.create_hands(10)
    new_game.player.hands[0] = Hand(10,[Card("A", "spades"),
                                        Card("J", "clubs")])
    new_game.payout_blackjack(new_game.player.hands[0])
    assert new_game.player.money == 125

    new_game.create_hands(10)
    assert new_game.player.money == 115
    new_game.player.hands[0] = Hand(10,[Card("2", "spades"),
                                        Card("J", "clubs")])
    new_game.dealer.hand = Hand(0,[Card("A", "spades"),
                                    Card("J", "clubs")])
    new_game.player.insured = True
    assert new_game.dealer.hand.get_value() == 21
    new_game.payout(new_game.player.hands[0], new_game.dealer.hand)
    assert new_game.player.money == 125

def test_get_available_actions():
    options = GameOptions()
    new_game = Game(options, "Alan")
    new_game.player.hands.append(Hand(10,[Card("2", "spades"),
                                          Card("J", "clubs")]))
    new_game.dealer.hand = Hand(0, [Card("J", "spades"), Card("7", "Clubs")])
    actions = new_game.get_available_actions(new_game.player.hands[0],
                                             new_game.dealer.get_show_card())
    assert actions["hit"]
    assert actions["double"]
    assert not actions["split"]
    assert not actions["surrender"]
    new_game.player.hands[0] = Hand(10,[Card("J", "spades"),
                                        Card("J", "clubs")])
    new_game.dealer.hand = Hand(0, [Card("A", "spades"), Card("7", "Clubs")])
    actions = new_game.get_available_actions(new_game.player.hands[0],
                                             new_game.dealer.get_show_card())

    assert actions["hit"]
    assert actions["double"]
    assert actions["split"]
    assert actions["surrender"]
