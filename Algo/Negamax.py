from Algo.Position import Position


class Negamax:

    def __init__(self):
        self.noeuds_parcourus = 0

    def negamax(self, pos: Position, alpha, beta):
        assert alpha < beta
        self.noeuds_parcourus += 1

        if self.checkDraw(pos):
            return 0

        for i in range(7):
            if pos.canPlay(i) and pos.isWinningMove(i):
                return (pos.WIDTH*pos.HEIGHT+1 - pos.nbMove())//2

        max = (pos.WIDTH*pos.HEIGHT-1-pos.nbMove())//2

        if beta > max:
            beta = max
            if alpha >= beta:
                return beta

        for x in range(7):
            if pos.canPlay(x):
                pos2 = Position(pos.coup_joue)
                pos2.play(x)

                score = -(self.negamax(pos2, -beta, -alpha))

                if score >= beta:
                    return score

                if score > alpha:
                    alpha = score

        return alpha

    def solve(self, pos: Position, weak=False):
        self.noeuds_parcourus = 0
        if weak:
            return self.negamax(pos, -1, 1)
        else:
            return self.negamax(pos, -pos.WIDTH*pos.HEIGHT//2, pos.WIDTH*pos.HEIGHT//2)

    def checkDraw(self, pos: Position):
        if pos.moves == pos.WIDTH*pos.HEIGHT:
            return True
        return False

    def getNodeCount(self):
        return self.noeuds_parcourus


if __name__ == "__main__":
    coup_joue = "7422341735647741166133573473242566"
    pos = Position(coup_joue)
    s = Negamax()
    print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n',"Score Final:",s.solve(pos))
