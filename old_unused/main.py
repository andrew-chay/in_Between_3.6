from Player import Player, Card, suits
import random

print "------------------------------------------"
print "          Welcome to In-Between!          "
print "------------------------------------------"
no_player = input("Enter Number of Players ---> ")
pot_size = input("Enter Total Pot Amount ---> $")

p_list = [Player("", 0, 0, 0, 0) for i in range(no_player)]

for x in p_list:
    x.name = raw_input("Enter Player's Name ---> ") 

def shuffle_deck():
    d1 = [Card(rank, suit) for rank in range(1,14) for suit in suits]
    random.shuffle(d1)
    return d1

deck = shuffle_deck()
bet = []
k = 1
print "\n"

while k < 17:
    for player in p_list:
        for draw in range(3):
            bet.append(deck.pop())
        print "----------%s, Current Earnings: $%d, Win/Loss/Fold: %d/%d/%d-----------" \
            % (player.name, player.score, player.win, player.lose, player.fold)
        print "------------Round %d, Current Pot: $%d, %d Cards Remain---------------\n" \
            % (k, pot_size, len(deck))
        print "The Cards drawn are " + bet[0].cardName() + " and " + bet[1].cardName()
        if (bet[0].rank == bet[1].rank) or (bet[0].rank - bet[1].rank == -1) or (bet[0].rank - bet[1].rank == 1):
            choice = raw_input("Both Cards have the same value / difference of 1, Bet Upper/Lower or Fold? (u / l / f) ---> ")
            if choice == "l":
                bet_amount = input("Enter Bet Amount ---> $")
                if(bet[0].rank > bet[2].rank):
                    print "You drew " + bet[2].cardName() + " which lower! You Win!\n"
                    pot_size -= bet_amount
                    player.win_round(bet_amount)
                    k += 1
                    del bet[:]
                elif bet[0].rank == bet[2].rank:
                    print "You drew " + bet[2].cardName() + " which is the same! You Lose Double!\n"
                    pot_size += bet_amount * 2
                    player.lose_round(bet_amount * 2)
                    k += 1
                    del bet[:]
                else:
                    print "You drew " + bet[2].cardName() + " which is higher! You Lose!\n"
                    pot_size += bet_amount
                    player.lose_round(bet_amount)
                    k += 1
                    del bet[:]
            elif choice == "u":
                bet_amount = input("Enter Bet Amount ---> $")
                if(bet[0].rank < bet[2].rank):
                    print "You drew " + bet[2].cardName() + " which higher! You Win!\n"
                    pot_size -= bet_amount
                    player.win_round(bet_amount)
                    k += 1
                    del bet[:]
                elif bet[0].rank == bet[2].rank:
                    print "You drew " + bet[2].cardName() + " which is has the same value! You Lose Double!\n"
                    pot_size += bet_amount * 2
                    player.lose_round(bet_amount * 2)
                    k += 1
                    del bet[:]
                else:
                    print "You drew " + bet[2].cardName() + " which is lower! You Lose!\n"
                    pot_size += bet_amount
                    player.lose_round(bet_amount)
                    k += 1
                    del bet[:]
            elif choice == "f":
                fold_amount = pot_size * 0.02
                player.fold_round(fold_amount)
                pot_size += fold_amount
                print "You folded, automatically losing $%d.\n" %(fold_amount)
                k += 1
                del bet[:]
                
        else:
            choice = raw_input("Will you Bet or Fold? (b / f) ---> ")
            if choice == "b":
                bet_amount = input("Enter Bet Amount ---> $")
                if (bet[0].rank < bet[2].rank < bet[1].rank) \
                        or (bet[0].rank > bet[2].rank > bet[1].rank):
                    print "You drew " + bet[2].cardName() + " which is in between! You Win!\n"
                    pot_size -= bet_amount
                    player.win_round(bet_amount)
                    k += 1
                    del bet[:]
                elif (abs(bet[0].rank - bet[2].rank) == 1) and (abs(bet[1].rank - bet[2].rank) == 1):
                    print "You drew " + bet[2].cardName() + " which is 3 in a row! You Win Double!\n"
                    pot_size -= bet_amount * 2
                    player.win_round(bet_amount * 2)
                    k += 1
                    del bet[:]
                elif (bet[2].rank == bet[0].rank) or (bet[2].rank == bet[1].rank):
                    print "You drew " + bet[2].cardName() + " which is has the same value! You Lose Double!\n"
                    pot_size += bet_amount * 2
                    player.lose_round(bet_amount * 2)
                    k += 1
                    del bet[:]
                else:
                    print "You drew " + bet[2].cardName() + " which is not in between! You Lose!\n"
                    pot_size += bet_amount
                    player.lose_round(bet_amount)
                    k += 1
                    del bet[:]
            else:
                fold_amount = pot_size * 0.02
                player.fold_round(fold_amount)
                pot_size += fold_amount
                print "You folded, automatically losing $%d.\n" %(fold_amount)
                k += 1
                del bet[:]

            if k == 17:
                cont = raw_input("Game has ended, Type c to continue, e to end ---> ")
                if cont == "c":
                    k = 1
                    deck = shuffle_deck()
                else:
                    print "-----------------Summary------------------"
                    for players in p_list:
                        players.summary()
                    print "------------------------------------------"
