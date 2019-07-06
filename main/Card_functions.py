CARD = """\
┌─────────┐
│{}       │
│         │
│         │
│    {}   │
│         │
│         │
│       {}│
└─────────┘
""".format('{rank: <2}', '{suit: <2}', '{rank: >2}')

def join_lines(strings):
    liness = [string.splitlines() for string in strings]
    return '\n'.join(''.join(lines) for lines in zip(*liness))

def card_graphics(*cards):
    name_to_symbol = {
        'Spades':   '♠',
        'Diamonds': '♦',
        'Hearts':   '♥',
        'Clubs':    '♣',
        '?': '?'
    }

    def card_to_string(card):
        rank = ""
        if card.rank == 1:
            rank = "A"
        elif card.rank == 10:
            rank = str(card.rank)
        elif card.rank == 11:
            rank = "J"
        elif card.rank == 12:
            rank = "Q"
        elif card.rank == 13:
            rank = "K"
        elif card.rank == 0:
            rank = "?"
        else:
            rank = str(card.rank)

        return CARD.format(rank=rank, suit=name_to_symbol[card.suit])

    return join_lines(map(card_to_string, cards))

def check_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a positive integer")
            continue

        if value < 0:
            print("Please enter a positive integer")
            continue
        else:
            break
    return value
