from Player3 import Player, Cards
from card_functions import *
from stats import *
import random, time

suits = ("Spades","Hearts","Clubs","Diamonds")
def shuffle_deck():
    d1 = [Cards(suit, rank) for suit in suits for rank in range(1,14)]
    random.shuffle(d1)
    return d1

valid1 = ["b","f"]
valid2 = ["h","l","f"]
test_card_1 = Cards('Diamonds', 1)
test_card_2 = Cards('Clubs', 11)
test_card_3 = Cards('Spades', 12)
test_card_4 = Cards('Hearts', 13) 
question_card = Cards('?', 0)
player_no = 1

print("--------------------------------------------")
print("            Welcome to In-Between!          ")
print(card_graphics(test_card_1, test_card_2, test_card_3, test_card_4))
print ("                 by kupori                 ")
print("--------------------------------------------")

no_player = check_int("Enter Number of Players ---> ")
pot_size = check_int("Enter Total Pot Amount ---> $")
House = Player("House", pot_size, 0, 0, 0)
min_bet_amount = check_int("Enter Minimum Bet/Fold Amount ---> $")
while min_bet_amount > House.score:
    min_bet_amount = check_int("Minimum Amount cannot exceed Pot! ---> $")

p_list = [Player("", 0, 0, 0, 0) for i in range(no_player)]

for x in p_list:
    x.name = input("Enter Player {0}'s Name ---> ".format(player_no))
    player_no += 1 

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
                choice = input("Please Enter A Valid Choice (h/l/f)---> ")
            if choice == "l":
                bet_amount = check_int("Enter Bet Amount ---> $")
                while bet_amount < min_bet_amount:
                    bet_amount = check_int("Bet Amount is too low! ---> $")
                while bet_amount > House.score:
                    bet_amount = check_int("Bet Amount cannot exceed Current Pot! ---> $")
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
                while bet_amount < min_bet_amount:
                    bet_amount = check_int("Bet Amount is too low! ---> $")
                while bet_amount > House.score:
                    bet_amount = check_int("Bet Amount cannot exceed Current Pot! ---> $")
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
                House.win_round(min_bet_amount)
                player.fold_round(min_bet_amount)
                print("You folded, automatically losing $%d.\n" %(min_bet_amount))
                rounds += 1
                del bet[:]
                time.sleep(2)
                
        else:
            calculate_stats_bf(bet, stats)
            bet.append(deck.pop())
            stats.remove(bet[2].rank)
            choice = input("Will You Bet or Fold? (b/f) ---> ")
            while (choice not in valid1):
                choice = input("Please enter a Valid Choice (b/f) ---> ")
            if choice == "b":
                bet_amount = check_int("Enter Bet Amount ---> $")
                while bet_amount < min_bet_amount:
                    bet_amount = check_int("Bet Amount is too low! ---> $")
                while bet_amount > House.score:
                    bet_amount = check_int("Bet Amount cannot exceed Current Pot! ---> $")
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
                House.win_round(min_bet_amount)
                player.fold_round(min_bet_amount)
                print("You folded, automatically losing $%d.\n" %(min_bet_amount))
                rounds += 1
                del bet[:]
                time.sleep(2)
            
        if House.score == 0:
            print ("The pot has been emptied")
            choice = input("Would you like to refill the pot? (y/n) ---> ")
            while choice not in ['y','n']:
                choice = input("Please Enter a Valid Choice (y/n) ---> ")
            if choice == "y":
                pot_size = check_int("Enter Total Pot Amount ---> $")
                House.score += pot_size
            else:
                rounds = t_rounds
                
            if rounds == t_rounds:
                cont = input("Game has ended, Type c to continue, e to end ---> ")
                if cont == "c":
                    t_rounds += 17
                    deck = shuffle_deck()
                    stats = statistics_deck ()
                    choice = input("Would you like to refill the pot? (y/n) ---> ")
                    while choice not in ['y','n']:
                        choice = input("Please Enter a Valid Choice (y/n) ---> ")
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

print ("Thank you for playing - kupori")
print("The Game will end in 3 seconds")
time.sleep(3)
