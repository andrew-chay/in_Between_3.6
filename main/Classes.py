class Player:
    def __init__(self, name, score, win, lose, fold):
        self.name = name
        self.score = score # current winnings / loss
        self.win = win 
        self.lose = lose
        self.fold = fold 
    
    def summary(self):
        if self.score >= 0:
            print("%s has won $%d and holds a Win/Loss/Fold score of %d/%d/%d" \
                % (self.name, self.score, self.win, self.lose, self.fold))
        else:
            print("%s has lost $%d and holds a Win/Loss/Fold score of %d/%d/%d" \
                % (self.name, self.score, self.win, self.lose, self.fold))

    def win_round(self, money):
        self.win += 1
        self.score += money

    def lose_round(self, money):
        self.lose += 1
        self.score -= money
    
    def fold_round(self, money):
        self.fold += 1
        self.score -= money

class Cards(object):

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def cardName(self):
        specialCards = {11: "Jack", 12: "Queen", 13:"King", 1: "Ace"}
        rank_name = specialCards[self.rank] if self.rank in specialCards else self.rank
        return '%s of %s'%(rank_name, self.suit)

        