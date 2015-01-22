from card import Card
from deck import Deck


print(Card.card_list)
dealer = Dealer()
player = Player(100) #start with 100 units of currency
game = Game(dealer, [player]) #create a game with 1 dealer and 1-player
game.reset_hands()
game.deal()
