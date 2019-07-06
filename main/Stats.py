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
    print(f"Odds of Hitting In Between is {ibt:.2f}%")

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
    print(f"Odds of Higher/Lower is {upper_odds:.2f}% / {lower_odds:.2f}%")