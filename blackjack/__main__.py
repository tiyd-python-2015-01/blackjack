
from blackjack.game import Game

if __name__ == '__main__':
    cardgame = Game()
    while cardgame.start_game():
        cardgame = Game()
    
