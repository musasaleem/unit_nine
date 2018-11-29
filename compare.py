import deck

def make_a_deck():
    deck_of_cards = deck.Deck()
    deck_of_cards.shuffle()
    return deck_of_cards


def draw(deck_of_cards):
    player = []
    for five in range(5):
        player.append(deck_of_cards.draw_a_card())
    return player

def compare(p1, p2):
    compare = p1.compared_to(p2)
    return compare


def main():
    deck_of_cards = make_a_deck()
    p1 = draw(deck_of_cards)
    p2 = draw(deck_of_cards)
    print(p1[five], p2[five])
    print((compare(p1[five], p2[five])))

main()