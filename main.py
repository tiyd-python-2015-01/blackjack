from deck import Deck
from shoe import Shoe
from hand import Hand
from player import Player


deck1 = Deck()

deck1.shuffle()


print("drawing {}".format(deck1.draw()))

player1 = Player("JOHNN")

player1.hit(deck1)
player1.hit(deck1)

print("THE HAND IS: {}".format(player1.hand))
print(player1.hand.hard_total)
