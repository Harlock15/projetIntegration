# Importation de la classe Position depuis le module Algo.Position
from Algo.Position import Position  
# Importation de la classe Transposition depuis le module Algo.Transposition
from Algo.Transposition import Transposition  


class Negamax:
    def __init__(self):
        # Initialisation du compteur de nœuds parcourus et de la table de transposition
        self.noeuds_parcourus = 0
        self.trans = Transposition()

    # Algorithme negamax pour trouver le meilleur coup
    def negamax(self, pos: Position, alpha, beta):
        assert alpha < beta  # Assertion pour vérifier que alpha est strictement inférieur à beta
        self.noeuds_parcourus += 1  # Incrémentation du compteur de nœuds parcourus

        # Vérification si la partie est nulle
        if self.checkDraw(pos):
            return 0

        # Vérification des coups gagnants
        for i in [3, 2, 4, 1, 5, 0, 6]:
            if pos.canPlay(i) and pos.isWinningMove(i):
                return (pos.WIDTH*pos.HEIGHT+1 - pos.nbMove()) // 2

        # Initialisation de la valeur maximale
        max = (pos.WIDTH*pos.HEIGHT-1-pos.nbMove()) // 2

        # Récupération de la valeur depuis la table de transposition
        val = self.trans.get(pos.getKey())
        if val:
            max = val + pos.MIN_SCORE - 1

        # Mise à jour de beta
        if beta > max:
            beta = max
            if alpha >= beta:
                return beta

        # Parcours des coups possibles
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

        # Mise à jour de la table de transposition
        self.trans.put(pos.getKey(), alpha - pos.MIN_SCORE + 1)
        return alpha

    # Méthode pour résoudre la position actuelle
    def solve(self, pos: Position, weak=False):
        # Initialisation des bornes inférieure et supérieure
        min = -(pos.WIDTH * pos.HEIGHT - pos.nbMove()) / 2
        max = (pos.WIDTH * pos.HEIGHT + 1 - pos.nbMove()) / 2
        if weak:
            min = -1
            max = 1
        while min < max:
            med = min + (max - min) // 2
            if 0 >= med > min // 2:
                med = min // 2
            elif max // 2 > med >= 0:
                med = max // 2
            res = self.negamax(pos, med, med + 1)
            if res <= med:
                max = res
            else:
                min = res
        return min

    # Méthode pour vérifier si la partie est nulle
    def checkDraw(self, pos: Position):
        if pos.moves == pos.WIDTH * pos.HEIGHT:
            return True
        return False

    # Méthode pour obtenir le nombre de nœuds parcourus
    def getNodeCount(self):
        return self.noeuds_parcourus


if __name__ == "__main__":
    # Exemple d'utilisation de la classe Negamax pour résoudre une position
    coup_joue = "42454611251266217126153276635"
    pos = Position()
    pos.initBoard(coup_joue)
    s = Negamax()
    print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
    print("Score Final:", s.solve(pos))
