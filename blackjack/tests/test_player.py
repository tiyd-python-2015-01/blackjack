from blackjack.player import Player
from blackjack.carddeckshoe import Card


def test_create_player():
    player = Player()

def test_get_hand():
    player = Player()
    player.get_hand([Card(2,"♢"),Card(2,"♡")])
    assert player.cards == [Card(2,"♢"), Card(2,"♡")]
    assert player.cash == 100

def test_get_card():
    player = Player()
    player.get_hand([Card(2,"♢"),Card(2,"♡")])
    player.get_card(Card(3,"♤"))
    assert len(player.cards) == 3
    player.get_card(Card(4,"♤"))
    assert len(player.cards) == 4

def test_assess_hand():
    player = Player()
    player.get_hand([Card(2,"♢"),Card(3,"♡")])
    assert player.assess_hand() == 5
    player.get_card(Card("Ace","♤"))
    assert player.assess_hand() == 16
    player.get_card(Card("Ace","♢"))
    assert player.assess_hand() == 17
    player.get_card(Card("Ace","♧"))
    assert player.assess_hand() == 18
    player.get_card(Card(10,"♧"))
    assert player.assess_hand() == 18
