from Algo.Position import Position
from Algo.Transposition import Transposition


class Negamax:

    def __init__(self):
        self.noeuds_parcourus = 0
        self.trans = Transposition()

    def negamax(self, pos: Position, alpha, beta):
        assert alpha < beta
        self.noeuds_parcourus += 1

        if self.checkDraw(pos):
            return 0

        for i in [3, 2, 4, 1, 5, 0, 6]:
            if pos.canPlay(i) and pos.isWinningMove(i):
                return (pos.WIDTH*pos.HEIGHT+1 - pos.nbMove())//2

        max = (pos.WIDTH*pos.HEIGHT-1-pos.nbMove())//2

        val = self.trans.get(pos.getKey())
        if val:
            max = val + pos.MIN_SCORE -1

        if beta > max:
            beta = max
            if alpha >= beta:
                return beta

        for x in [3, 2, 4, 1, 5, 0, 6]:
            if pos.canPlay(x):
                pos2 = Position()
                pos2.initPos(pos)
                pos2.play(x)

                score = -(self.negamax(pos2, -beta, -alpha))

                if score >= beta:
                    return score

                if score > alpha:
                    alpha = score

        self.trans.put(pos.getKey(), alpha - pos.MIN_SCORE + 1)
        return alpha

    def solve(self, pos: Position, weak=False):
        min = -(pos.WIDTH*pos.HEIGHT - pos.nbMove())/2
        max = (pos.WIDTH*(pos.HEIGHT + 1) - pos.nbMove())/2
        if weak:
            min = -1
            max = 1
        while min < max:
            med = min + (max - min)/2
            if 0 >= med > min/2:
                med = min/2
            elif max/2 > med >= 0:
                med = max/2
            res = self.negamax(pos, med, med + 1)
            if res <= med:
                max = res
            else:
                min = res
        return min

    def checkDraw(self, pos: Position):
        if pos.moves == pos.WIDTH*pos.HEIGHT:
            return True
        return False

    def getNodeCount(self):
        return self.noeuds_parcourus


if __name__ == "__main__":
    coup_joue = "42454611251266217126153276635"
    pos = Position()
    pos.initBoard(coup_joue)
    s = Negamax()
    print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n', "Score Final:", s.solve(pos))
