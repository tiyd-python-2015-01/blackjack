from blackjack.dealer import Dealer
from blackjack.deck import Deck

dealer = Dealer()
deck = Deck()


def test_dealer_hand():
    dealer.take_card(deck)
    dealer.put_face_down(deck)
    assert len(dealer.hand) == 1
    assert len(dealer.face_down) == 1
    dealer.reveal()
    assert len(dealer.face_down) == 0
    assert len(dealer.hand) == 2
