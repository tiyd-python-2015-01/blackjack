# Blackjack

Blackjack is a game played between a Dealer and a Player.

1. At the start of the game, the Player has the choice of how many Decks they would like in the Shoe.  The choice is from 1-6.

2. Cards are dealt from a Shoe that consists of one or more Decks.
These cards constitute the Hands of each player, PlayerHand and DealerHand.
At the start of the Game, 2 cards are dealt to each player (The 1st and 3rd cards off the deck go to the player.  The 2nd and 4th cards go to the dealer.)

3.  The player's PointTotal is the combined points of his hand.  The dealer's PointTotal is the combined points of his hand.

4. Points are ascribed as follows:
  The ace is worth 11 points, unless the PointTotal of the hand with an 11-point ace is worth more than 21.  In that case, it is worth 1 point.
  2-10 are worth the same points as their names
  Face cards (Jack, Queen, King) are worth 10 points

5. After the cards are dealt, the first Round takes place:

ROUND:
a.  the Player has the choice to Hit or Stay.  Hitting means that another Card is drawn from the Shoe, the Card is added to the player's hand and the points from that card are added to the PointTotal of the Player's Hand.  Stay means that no more cards are drawn, and his PointTotal remains at its current amount.  Stay also means that he stays for all future rounds.

b. After the player acts, there should be a win-condition check to see if the player has busted.  If the player hit and busted, the dealer wins.

c. If the player has not busted, the Dealer either hits or stays based on its built in hit-or-stay algorithm.  If the TotalPoints in DealerHand are less than 17, the Dealer will Hit.  If the TotalPoints in DealerHand are greater than 17, the Dealer will Stay. (If the dealer has an ace and TotalPoints == 17, then the Dealer hits.)  If the dealer hits, another card is added to the player's Hand and the hand's PointTotal are increased by the point value of the card card.  

d. After Dealer plays, another win-condition check.  If the player's last move was stay, and the Dealer's hand is greater than 17, the game ends.  Whoever's hand has the greater PointTotal is the winner.
If the Dealer hits and busts(PointTotal greater than 21), the player wins.

6. Repeat Rounds until one of the win conditions is met
