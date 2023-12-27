from Algo.Position import Position

class Negamax:

    def __init__(self):
        self.noeuds_parcourus = 0


    def negamax(self, pos:Position):
        self.noeuds_parcourus+=1

        if(self.checkDraw(pos)):
            return 0

        for i in range(7):
            if(pos.canPlay(i) and pos.isWinningMove(i)):
                return ((pos.WIDTH*pos.HEIGHT+1 - pos.nbMove())//2)

        self.best_score = -(pos.WIDTH*pos.HEIGHT)

        for x in range(7):
            if(pos.canPlay(x)):

                pos2 = Position(pos.coup_joue)

                pos2.play(x)

                score = -(self.negamax(pos2))

                if(score > self.best_score):
                    self.best_score = score

        return self.best_score


    def checkDraw(self, pos:Position):
        if(pos.moves == pos.WIDTH*pos.HEIGHT):
            return True
        return False


if __name__=="__main__":
    coup_joue = "65214673556155731566316327373221417"
    pos = Position(coup_joue)
    pos.affBoard()
    s = Negamax()
    print("Score :",s.negamax(pos))
