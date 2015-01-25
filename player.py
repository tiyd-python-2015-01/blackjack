from deck import Deck

class Player:
    """Player class: holds a hand, gets cards, places bets and has a pot of
    money."""

    def __init__(self,deck):

        self.hand = []
        self.deck = deck

    def get_hand(self):
        """ Gets two random cards from deck, used for the first hand."""
        for _ in range(0,2):
            self.hand.append(self.deck.get_card())


    def __len__(self):
        """Shows the number of cards in the players hand."""

        return len(self.hand)

    def hit(self):
        """Pulls one random card from the deck, used to 'hit' in blackjack."""

        self.hand.append(self.deck.get_card())

    def get_value(self):
        """Adds up the value in the hand. If the hand is greater than 10, aces
        are worth 1, else they are worth 11."""

        total_value = 0
        for card in self.hand:
            if card.number in list("23456789")+["10"]:
                value = int(card.number)
                total_value += value
            elif card.number in ["Jack","King","Queen"]:
                value = 10
                total_value += value
            elif card.number == "Ace":
                if total_value > 10:
                    value = 1
                    total_value += value
                else:
                    value = 11
                    total_value += value

        return total_value


    def view_cards(self):
        """Prints cards in the players hand."""

        for card in self.hand:
            print(card)
        print("\n")


class Dealer(Player):
    """Dealer class: holds a hand, draws and prints cards."""

    def __init__(self, deck):
        """Overwriting player init to not include pot"""
        self.hand = []
        self.deck = deck

    def view_cards(self):
        """Prints cards, with one face down"""
        print("xxx \n")
        for card in self.hand[1:]:
            print(card)
            print("\n")

#new_deck = Deck()
# new_player = Player(100,new_deck)
# new_player.get_hand()
# new_player.view_cards()
# new_player.hit()
# new_player.view_cards()
# print(new_player.get_value())
# new_dealer = Dealer(100,new_deck)
# new_dealer.get_hand()
# new_dealer.view_cards()
# print(len(new_dealer))
