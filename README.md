# Blackjack

Players can start the game in their console by typing:
python -m blackjack

Blackjack is a game played between a Dealer and a Player.

1. Cards are dealt from a deck that reshuffles after each hand.
These cards constitute the Hands of each player.
At the start of the Game, 2 cards are dealt to each player (The 1st and 3rd cards off the deck go to the player.  The 2nd and 4th cards go to the dealer.)

2.  The player's point total is the combined points of his hand.  The dealer's point total is the combined points of his hand.

3. Points are ascribed as follows:
  The ace is worth 11 points, unless the point total of the hand with an 11-point ace is worth more than 21.  In that case, it is worth 1 point.
  2-10 are worth the same points as their names
  Face cards (Jack, Queen, King) are worth 10 points

4. The player acts first. The Player has the choice to Hit or Stand.  Hitting means that another Card is drawn from the deck, the Card is added to the player's hand and the points from that card are added to the point total of the Player's Hand.  Stand means that no more cards are drawn, and his point total remains at its current amount.  Stay also means that he stays for all future rounds.

5. After the player acts, there should be a win-condition check to see if the player has busted.  If the player hit and busted, the dealer wins.

6. If the player has not busted, the Dealer either hits or stays based on its built in hit-or-stay algorithm.  If the total points in DealerHand are less than 17, the Dealer will Hit.  If the total points in DealerHand are greater than 17, the Dealer will Stay. (If the dealer has an ace and TotalPoints == 17, then the Dealer hits.)  If the dealer hits, another card is added to the player's Hand and the hand's point total are increased by the point value of the card card.  

7. After Dealer plays, another win-condition check.  If the dealer busted, the player wins.  If neither player nor dealer busted, whoever's hand is higher wins.  A tie is called a push.

8. If the player wins, he wins the amount of his bet.  If he loses, he loses the amount of his bet.  If it is a push, there is no change to the amount of the player's chips.  If the players wins with blackjack, he wins 1.5x the amount of his bet.
