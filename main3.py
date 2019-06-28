from Player3 import Player, Cards, suits
import random, time

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

def shuffle_deck():
    d1 = [Cards(suit, rank) for suit in suits for rank in range(1,14)]
    random.shuffle(d1)
    return d1

def statistics_deck():
    s1 = [i for i in range(1,14) for x in range(1,5)]
    return sorted(s1)
    
def remove_card_from_stats(d1, s1):
    s1.remove(d1[0].rank)
    s1.remove(d1[1].rank)

def calculate_stats_bf(d1, s1):
    win = 0
    for i in range(0,len(s1)):
        if d1[0].rank < s1[i] < d1[1].rank or \
            d1[0].rank > s1[i] > d1[1].rank:
            win += 1
    if win > 0:
        ibt = (win/len(s1)) * 100
    else:
        ibt = 0.00
    print(f"Your odds of hitting In Between is {ibt:.2f}%")

def calculate_stats_ulf(d1, s1):
    upper = 0
    lower = 0
    if d1[0].rank == d1[1].rank:
        for i in range(0,len(s1)):
            if s1[i] < d1[0].rank:
                lower += 1
            elif s1[i] > d1[0].rank:
                upper += 1
    elif (d1[0].rank - d1[1].rank == -1) or (d1[0].rank - d1[1].rank == 1):
        for i in range(0,len(s1)):
            if d1[0].rank > d1[1].rank:
                if s1[i] < d1[1].rank:
                    lower += 1
                elif s1[i] > d1[0].rank:
                    upper += 1
            elif d1[0].rank < d1[1].rank:
                if s1[i] < d1[0].rank:
                    lower += 1
                elif s1[i] > d1[1].rank:
                    upper += 1
    if upper > 0:
        upper_odds = (upper/len(s1)) * 100
    else:
        upper_odds = 0.00
    if lower > 0:
        lower_odds = (lower/len(s1)) * 100
    else:
        lower_odds = 0.00
    print(f"Your odds of Higher/Lower is {upper_odds:.2f}% and {lower_odds:.2f}%")

valid1 = ["b","f"]
valid2 = ["h","l","f"]
test_card_1 = Cards('Diamonds', 1)
test_card_2 = Cards('Clubs', 11)
test_card_3 = Cards('Spades', 12)
test_card_4 = Cards('Hearts', 13) 
question_card = Cards('?', 0)

print("------------------------------------------")
print("          Welcome to In-Between!          ")
print(card_graphics(test_card_1, test_card_2, test_card_3, test_card_4))
print("------------------------------------------")

no_player = check_int("Enter Number of Players ---> ")
pot_size = check_int("Enter Total Pot Amount ---> $")
House = Player("House", pot_size, 0, 0, 0)

p_list = [Player("", 0, 0, 0, 0) for i in range(no_player)]

for x in p_list:
    x.name = input("Enter Player's Name ---> ") 

stats = statistics_deck()
deck = shuffle_deck()
bet = []
rounds = 1
t_rounds = 18
print("\n")

while rounds < t_rounds:
    for player in p_list:
        for draw in range(2):
            bet.append(deck.pop())
        remove_card_from_stats(bet, stats)
        print("----------%s, Current Earnings: $%d, Win/Loss/Fold: %d/%d/%d-----------" \
            % (player.name, player.score, player.win, player.lose, player.fold))
        print("------------Round %d, Current Pot: $%d, %d Cards Remain---------------\n" \
            % (rounds, House.score, len(deck)))
        print("Drew " + bet[0].cardName() + " and " + bet[1].cardName())
        print (card_graphics(bet[0],question_card, bet[1]))

        if (bet[0].rank == bet[1].rank) or (bet[0].rank - bet[1].rank == -1) or (bet[0].rank - bet[1].rank == 1):
            calculate_stats_ulf(bet, stats)
            bet.append(deck.pop())
            stats.remove(bet[2].rank)
            choice = input("Bet Higher/Lower or Fold? (h/l/f)---> ")
            while (choice not in valid2):
                choice = input("Please enter a valid choice (h/l/f)---> ")
            if choice == "l":
                bet_amount = check_int("Enter Bet Amount ---> $")
                time.sleep(1)
                if(bet[0].rank > bet[2].rank):
                    print(card_graphics(bet[2]))
                    print("You drew " + bet[2].cardName() + " which lower! You Win!\n")
                    House.lose_round(bet_amount)
                    player.win_round(bet_amount)
                    rounds += 1
                    del bet[:]
                    time.sleep(2)
                elif (bet[2].rank == bet[0].rank) or (bet[2].rank == bet[1].rank):
                    print(card_graphics(bet[2]))
                    print("You drew " + bet[2].cardName() + " which has the same value! You Lose Double!\n") 
                    House.win_round(bet_amount * 2)
                    player.lose_round(bet_amount * 2)
                    rounds += 1
                    del bet[:]
                    time.sleep(2)
                else:
                    print(card_graphics(bet[2]))
                    print("You drew " + bet[2].cardName() + " which is higher! You Lose!\n")
                    House.win_round(bet_amount)
                    player.lose_round(bet_amount)
                    rounds += 1
                    del bet[:]
                    time.sleep(2)
            elif choice == "h":
                bet_amount = check_int("Enter Bet Amount ---> $")
                time.sleep(1)
                if(bet[0].rank < bet[2].rank):
                    print(card_graphics(bet[2]))
                    print("You drew " + bet[2].cardName() + " which higher! You Win!\n")
                    House.lose_round(bet_amount)
                    player.win_round(bet_amount)
                    rounds += 1
                    del bet[:]
                    time.sleep(2)
                elif (bet[2].rank == bet[0].rank) or (bet[2].rank == bet[1].rank):
                    print(card_graphics(bet[2]))
                    print("You drew " + bet[2].cardName() + " which has the same value! You Lose Double!\n")
                    House.win_round(bet_amount * 2)
                    player.lose_round(bet_amount * 2)
                    rounds += 1
                    del bet[:]
                    time.sleep(2)
                else:
                    time.sleep(1)
                    print(card_graphics(bet[2]))
                    print("You drew " + bet[2].cardName() + " which is lower! You Lose!\n")
                    House.win_round(bet_amount)
                    player.lose_round(bet_amount)
                    rounds += 1
                    del bet[:]
                    time.sleep(2)
            elif choice == "f":
                time.sleep(1)
                fold_amount = pot_size * 0.02
                House.win_round(fold_amount)
                player.fold_round(fold_amount)
                print("You folded, automatically losing $%d.\n" %(fold_amount))
                rounds += 1
                del bet[:]
                time.sleep(2)
                
        else:
            calculate_stats_bf(bet, stats)
            bet.append(deck.pop())
            stats.remove(bet[2].rank)
            choice = input("Will You Bet or Fold? (b/f) ---> ")
            while (choice not in valid1):
                choice = input("Please enter a valid choice (b/f) ---> ")
            if choice == "b":
                bet_amount = check_int("Enter Bet Amount ---> $")
                time.sleep(1)
                if (bet[0].rank < bet[2].rank < bet[1].rank) \
                        or (bet[0].rank > bet[2].rank > bet[1].rank):
                    print(card_graphics(bet[2]))
                    print("You drew " + bet[2].cardName() + " which is in between! You Win!\n")
                    House.lose_round(bet_amount)
                    player.win_round(bet_amount)
                    rounds += 1
                    del bet[:]
                    time.sleep(2)
                elif (abs(bet[0].rank - bet[2].rank) == 1) and (abs(bet[1].rank - bet[2].rank) == 1):
                    print(card_graphics(bet[2]))
                    print("You drew " + bet[2].cardName() + " which is 3 in a row! You Win Double!\n")
                    House.lose_round(bet_amount * 2)
                    player.win_round(bet_amount * 2)
                    rounds += 1
                    del bet[:]
                    time.sleep(2)
                elif (bet[2].rank == bet[0].rank) or (bet[2].rank == bet[1].rank):
                    print(card_graphics(bet[2]))
                    print("You drew " + bet[2].cardName() + " which has the same value! You Lose Double!\n")
                    House.win_round(bet_amount * 2)
                    player.lose_round(bet_amount * 2)
                    rounds += 1
                    del bet[:]
                    time.sleep(2)
                else:
                    print(card_graphics(bet[2]))
                    print("You drew " + bet[2].cardName() + " which is not in between! You Lose!\n")
                    House.win_round(bet_amount * 2)
                    player.lose_round(bet_amount)
                    rounds += 1
                    del bet[:]
                    time.sleep(2)
            elif choice == "f":
                fold_amount = pot_size * 0.02
                House.win_round(fold_amount)
                player.fold_round(fold_amount)
                print("You folded, automatically losing $%d.\n" %(fold_amount))
                rounds += 1
                del bet[:]
                time.sleep(2)

            if rounds == t_rounds:
                cont = input("Game has ended, Type c to continue, e to end ---> ")
                if cont == "c":
                    t_rounds += 17
                    deck = shuffle_deck()
                    stats = statistics_deck ()
                    choice = input("Would you like to refill the pot? (y/n) ---> ")
                    while choice not in ['y','n']:
                        choice = input("Please enter a valid choice (y/n) ---> ")
                    if choice == "y":
                        pot_size = check_int("Enter Total Pot Amount ---> $")
                        House.score += pot_size
                    else:
                        pass
                    print ("\n")
                else:
                    print("-----------------Summary------------------")
                    for players in p_list:
                        players.summary()
                    print("------------------------------------------")
                    print("The Game will close in 3 seconds")
                    time.sleep(3)
