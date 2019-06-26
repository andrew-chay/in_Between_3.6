from Player3 import Player, Cards, suits
import random

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

test_card_1 = Cards('Diamonds', 1)
test_card_2 = Cards('Clubs', 11)
test_card_3 = Cards('Spades', 12)
test_card_4 = Cards('Hearts', 13) 
question_card = Cards('?', 0)

print("------------------------------------------")
print("          Welcome to In-Between!          ")
print(card_graphics(test_card_1, test_card_2, test_card_3, test_card_4))
print("------------------------------------------")

no_player = eval(input("Enter Number of Players ---> "))
pot_size = eval(input("Enter Total Pot Amount ---> $"))

p_list = [Player("", 0, 0, 0, 0) for i in range(no_player)]

for x in p_list:
    x.name = input("Enter Player's Name ---> ") 

def shuffle_deck():
    d1 = [Cards(suit, rank) for suit in suits for rank in range(1,14)]
    random.shuffle(d1)
    return d1

deck = shuffle_deck()
bet = []
k = 1
print("\n")

while k < 17:
    for player in p_list:
        for draw in range(3):
            bet.append(deck.pop())
        print("----------%s, Current Earnings: $%d, Win/Loss/Fold: %d/%d/%d-----------" \
            % (player.name, player.score, player.win, player.lose, player.fold))
        print("------------Round %d, Current Pot: $%d, %d Cards Remain---------------\n" \
            % (k, pot_size, len(deck)))
        print("Drew " + bet[0].cardName() + " and " + bet[1].cardName())
        print (card_graphics(bet[0],question_card, bet[1]))

        if (bet[0].rank == bet[1].rank) or (bet[0].rank - bet[1].rank == -1) or (bet[0].rank - bet[1].rank == 1):
            choice = input("Both Cards have the same value / difference of 1, Bet Upper/Lower or Fold? (u / l / f) ---> ")
            if choice == "l":
                bet_amount = eval(input("Enter Bet Amount ---> $"))
                if(bet[0].rank > bet[2].rank):
                    print(card_graphics(bet[2]))
                    print("You drew " + bet[2].cardName() + " which lower! You Win!\n")
                    pot_size -= bet_amount
                    player.win_round(bet_amount)
                    k += 1
                    del bet[:]
                elif bet[0].rank == bet[2].rank:
                    print(card_graphics(bet[2]))
                    print("You drew " + bet[2].cardName() + " which is the same! You Lose Double!\n")
                    pot_size += bet_amount * 2
                    player.lose_round(bet_amount * 2)
                    k += 1
                    del bet[:]
                else:
                    print(card_graphics(bet[2]))
                    print("You drew " + bet[2].cardName() + " which is higher! You Lose!\n")
                    pot_size += bet_amount
                    player.lose_round(bet_amount)
                    k += 1
                    del bet[:]
            elif choice == "u":
                bet_amount = eval(input("Enter Bet Amount ---> $"))
                if(bet[0].rank < bet[2].rank):
                    print(card_graphics(bet[2]))
                    print("You drew " + bet[2].cardName() + " which higher! You Win!\n")
                    pot_size -= bet_amount
                    player.win_round(bet_amount)
                    k += 1
                    del bet[:]
                elif bet[0].rank == bet[2].rank:
                    print(card_graphics(bet[2]))
                    print("You drew " + bet[2].cardName() + " which is has the same value! You Lose Double!\n")
                    pot_size += bet_amount * 2
                    player.lose_round(bet_amount * 2)
                    k += 1
                    del bet[:]
                else:
                    print(card_graphics(bet[2]))
                    print("You drew " + bet[2].cardName() + " which is lower! You Lose!\n")
                    pot_size += bet_amount
                    player.lose_round(bet_amount)
                    k += 1
                    del bet[:]
            elif choice == "f":
                fold_amount = pot_size * 0.02
                player.fold_round(fold_amount)
                pot_size += fold_amount
                print("You folded, automatically losing $%d.\n" %(fold_amount))
                k += 1
                del bet[:]
                
        else:
            choice = input("Will You Bet or Fold? (b / f) ---> ")
            if choice == "b":
                bet_amount = eval(input("Enter Bet Amount ---> $"))
                if (bet[0].rank < bet[2].rank < bet[1].rank) \
                        or (bet[0].rank > bet[2].rank > bet[1].rank):
                    print(card_graphics(bet[2]))
                    print("You drew " + bet[2].cardName() + " which is in between! You Win!\n")
                    pot_size -= bet_amount
                    player.win_round(bet_amount)
                    k += 1
                    del bet[:]
                elif (abs(bet[0].rank - bet[2].rank) == 1) and (abs(bet[1].rank - bet[2].rank) == 1):
                    print(card_graphics(bet[2]))
                    print("You drew " + bet[2].cardName() + " which is 3 in a row! You Win Double!\n")
                    pot_size -= bet_amount * 2
                    player.win_round(bet_amount * 2)
                    k += 1
                    del bet[:]
                elif (bet[2].rank == bet[0].rank) or (bet[2].rank == bet[1].rank):
                    print(card_graphics(bet[2]))
                    print("You drew " + bet[2].cardName() + " which is has the same value! You Lose Double!\n")
                    pot_size += bet_amount * 2
                    player.lose_round(bet_amount * 2)
                    k += 1
                    del bet[:]
                else:
                    print(card_graphics(bet[2]))
                    print("You drew " + bet[2].cardName() + " which is not in between! You Lose!\n")
                    pot_size += bet_amount
                    player.lose_round(bet_amount)
                    k += 1
                    del bet[:]
            else:
                fold_amount = pot_size * 0.02
                player.fold_round(fold_amount)
                pot_size += fold_amount
                print("You folded, automatically losing $%d.\n" %(fold_amount))
                k += 1
                del bet[:]

            if k == 17:
                cont = input("Game has ended, Type c to continue, e to end ---> ")
                if cont == "c":
                    k = 1
                    deck = shuffle_deck()
                else:
                    print("-----------------Summary------------------")
                    for players in p_list:
                        players.summary()
                    print("------------------------------------------")

