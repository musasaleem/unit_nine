# Name: Musa Saleem
# Date: 12/3/18
# Last Modified: 12/3/18
# This program is a game of comparing cards between player 1 and player 2. The cards vary from the lowest, Ace of Spades
#  to the highest, King of Clubs. This program tallies up the points between 5 games and tells us who the
# ultimate winner is.

import deck


def make_a_deck():
    """
    This is importing the deck of cards and shuffling them
    :return: the shuffled deck of 52 playing cards
    """
    deck_of_cards = deck.Deck()
    deck_of_cards.shuffle()
    return deck_of_cards


def draw(deck_of_cards):
    """
    Gives the cards to the players
    :param deck_of_cards: shuffled deck of 52 cards
    :return: five cards for each player
    """
    player = []
    for five in range(5):
        player.append(deck_of_cards.draw_a_card())
    return player


def compare(card1, card2):
    """
    function for comparing cards
    :param card1: a single playing card
    :param card2: a single playing card
    :return: The higher of the two cards
    """
    return card1.compared_to(card2)


def main():  # main function
    p1_score = 0  # starting final score for player 1
    p2_score = 0  # starting final score for player 2
    deck_of_cards = make_a_deck()  # making the deck of cards
    p1 = draw(deck_of_cards)  # having player 1 drawing from the deck of cards
    p2 = draw(deck_of_cards)  # having player 2 drawing from the deck of cards
    for x in range(5):  # giving the x in range to be 5 so each player draws five cards
        com = compare(p1[x], p2[x])  # comparing the first card for player one and player 2
        print("Player 1:", p1[x])  # giving the value of the first card for player 1
        print("Player 2:", p2[x])  # giving the value of the first card for player 2
        print("  ")  # A blank line so it looks prettier
        if com == p1[x]:  # This is an if statement saying if player 1 wins the round
            p1_score += 1  # adds a point to the total value of player 1
            print("player 1 wins this round, cash money")  # The print statement saying that player 1 won the round
            print()  # A blank line so it looks prettier
        elif com == p2[x]: # This is an if statement saying if player 2 wins the round
            p2_score += 1  # adds a point to the total value of player 2
            print("player 2 wins this round, cash money")  # The print statement saying that player 2 won the round
            print()  # A blank line so it looks prettier
    if p1_score > p2_score:  # an if statement saying if player 1's total value is higher than player 2's
        print()  # A blank line so it looks prettier
        print("Player one wins the game, big baller brand")  # The print statement saying that player one wins the game
    else:  # an else statement saying if player 2's total value is higher than player 1's
        print()  # A blank line so it looks prettier
        print("Player two wins the game, big baller brand")  # The print statement saying that player two wins the game


main()  # Main loop
