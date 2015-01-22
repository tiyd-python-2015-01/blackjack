from deck import Deck
from shoe import Shoe
from hand import Hand
from player import Player


deck1 = Deck()

deck1.shuffle()
print(deck1)

card1 = deck1.draw()
card2 = deck1.draw()
card3 = deck1.draw()

print("drawing {}".format(deck1.draw()))

hand = Hand([card1, card2, card3])
player1 = Player("JOHNN", hand)

player1.hit(deck1)

print("THE HAND IS: {}".format(player1.hand))
