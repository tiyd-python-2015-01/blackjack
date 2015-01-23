from blackjack.card import Card


def checker_for_letters(prompt):
    """Way to check to make sure that the player is inputting any input that
    requires letters."""
    response = input(prompt)
    response = response.upper()
    if mode == "":
        print("You entered nothing, please try again.")
        return checker_for_words()
    if len(response) > 1:
        print("You entered more than one character. Please try again.")
        return checker_for_words()
    if not response.isalpha():
        print("You did not enter a letter, please try again.")
    return response


def value_checker(hand):
    """Checks to see what the value of a hand is. Goes through the whole hand
    and finds the values of each card other than an ace"""
    face_cards = ["Jack", "Queen", "King"]
    hand_value = 0
    for card in hand:
        if card.rank.isdigit():
            hand_value += int(card.rank)
        elif card.rank in face_cards:
            hand_value += 10
    for card in hand:
        if card.rank == "Ace":
            if hand_value > 10:
                hand_value += 1
            else:
                hand_value += 11
    return hand_value


def check_bust(hand):
    """Returns True if the value of the hand is greater than 21. False if it
    is less than 21."""
    return value_checker(hand) > 21


def win_check(hand):
    """Returns True if the value of the hand is 21 or not."""
    return value_checker(hand) == 21
