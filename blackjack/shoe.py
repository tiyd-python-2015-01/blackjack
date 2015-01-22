from deck import Deck


class Shoe(Deck):
    def __init__(self, number_of_decks):
        self.shoe = Deck()*number_of_decks
