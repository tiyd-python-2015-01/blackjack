from card import Card

def test_create_card():
    Card1 = Card(2, 'Spades')
    assert Card1.rank == 2
    assert Card1.suit == 'Spades'
