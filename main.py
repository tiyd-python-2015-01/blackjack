from deck import Deck
from shoe import Shoe

deck1 = Deck()
shoe1 = Shoe(6)


print(deck1.cards[3])
print(deck1)
print(shoe1)
shoe1.shuffle()
print(shoe1.shuffle())
