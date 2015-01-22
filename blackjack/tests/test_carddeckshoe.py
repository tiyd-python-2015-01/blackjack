import carddeckshoe as cds


def test_create_card():
    card1 = cds.Card(10, "Club")
    card2 = cds.Card("King", "Diamond")
    assert card1.face == 10
    assert card1.suit == "Club"
    assert card2.face == "King"
    assert card2.suit == "Diamond"


def test_create_deck():
    """Test if 52 Cards are created"""
    deck = cds.Deck()
    assert len(deck.cards) == 52
    assert isinstance(deck.cards[0], cds.Card)


def test_get_card():
    deck = cds.Deck()
    assert isinstance(deck.get_card(), cds.Card)
    assert len(deck.cards) == 51
    assert isinstance(deck.get_card(), cds.Card)
    assert len(deck.cards) == 50


def test_create_shoe():
    shoe = cds.Shoe()
    assert len(shoe.decks) == 1
    shoe = cds.Shoe(3)
    assert len(shoe.cards) == 156
    assert isinstance(shoe.cards[0], cds.Card)


def test_shuffle_shoe():
    shoe = cds.Shoe()
    card = shoe.cards[0]
    shoe.shuffle_shoe()
    assert shoe.cards[0] != card
    assert shoe.cards.index(card) >= 0
