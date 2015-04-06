from blackjack.deck import Deck


def test_deck_class():
    new_deck = Deck()
    assert len(new_deck.cards) == 52
    new_card = new_deck.deal_card()
    assert len(new_deck.cards) == 51
