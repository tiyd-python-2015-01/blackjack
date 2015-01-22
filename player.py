from deck import Deck

class Player:

    def __init__(self,pot,deck):

        self.hand = []
        self.pot = pot
        self.deck = deck

    def get_hand(self):
     for _ in range(0,2):
        self.hand.append(self.deck.get_card())


    def __len__(self):
        return len(self.hand)

    def hit(self):
        self.hand.append(self.deck.get_card())

    def get_value(self):
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
                    value = 10
                    total_value += value

        return total_value

    def bet(self):
        self.pot -= 10

    def view_cards(self):
        for card in self.hand:
            print(card)
        print("\n")


class Dealer(Player):

    def view_cards(self):
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
