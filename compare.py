import deck


def make_a_deck():
    deck_of_cards = deck.Deck()
    deck_of_cards.shuffle()
    return deck_of_cards


def draw(deck_of_cards):
    player = []
    for five in range(5a):
        player.append(deck_of_cards.draw_a_card())
    return player


def compare(card1, card2):
    return card1.compared_to(card2)


def main():
    deck_of_cards = make_a_deck()
    p1 = draw(deck_of_cards)
    p2 = draw(deck_of_cards)
    for x in range(5):
        com = compare(p1[x], p2[x])
        print("Player 1:", p1[x])
        print("Player 2:", p2[x])
        print("  ")
        if com == p1[x]:
            print("player 1 wins")
            print()
        elif com == p2[x]:
            print("player 2 wins")
            print()
        elif com == p2[x] == p1[x]:
            print("Big tie")


main()
