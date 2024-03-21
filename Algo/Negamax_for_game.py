from Algo.Position import Position  # Importation de la classe Position depuis le module Algo.Position
from Algo.Transposition import Transposition  # Importation de la classe Transposition depuis le module Algo.Transposition


class Negamax:
    def __init__(self):
        # Initialisation du compteur de nœuds parcourus et de la table de transposition
        self.noeuds_parcourus = 0
        self.trans = Transposition()

    # Algorithme negamax pour trouver le meilleur coup
    def negamax(self, pos: Position, alpha, beta, depth):
        assert alpha < beta  # Assertion pour vérifier que alpha est strictement inférieur à beta
        self.noeuds_parcourus += 1  # Incrémentation du compteur de nœuds parcourus

        # Vérification si la partie est nulle ou si la profondeur maximale est atteinte
        if depth <= 0 or self.checkDraw(pos):
            return 0, -1  # Retourne 0 pour le score et -1 pour la colonne (aucun coup)

        # Vérification des coups gagnants
        for i in [3, 2, 4, 1, 5, 0, 6]:
            if pos.canPlay(i) and pos.isWinningMove(i):
                return (pos.WIDTH * pos.HEIGHT + 1 - pos.nbMove()) // 2, i  # Retourne le score et la colonne du coup gagnant

        # Initialisation de la valeur maximale
        max = (pos.WIDTH * pos.HEIGHT - 1 - pos.nbMove()) // 2

        # Récupération de la valeur depuis la table de transposition
        val = self.trans.get(pos.getKey())
        if val:
            max = val + pos.MIN_SCORE - 1

        # Mise à jour de beta
        if beta > max:
            beta = max
            if alpha >= beta:
                return beta, -1  # Retourne beta pour le score et -1 pour la colonne (aucun coup)

        # Initialisation de la colonne du meilleur coup
        col = 1
        # Parcours des coups possibles
        for x in [3, 2, 4, 1, 5, 0, 6]:
            if pos.canPlay(x):
                pos2 = Position()
                pos2.initPos(pos)
                pos2.play(x)

                score, _ = self.negamax(pos2, -beta, -alpha, depth - 1)
                score = -score
                if score >= beta:
                    return score, x  # Retourne le score et la colonne du meilleur coup

                if score > alpha:
                    alpha = score
                    col = x  # Mise à jour de la colonne du meilleur coup

        # Mise à jour de la table de transposition
        self.trans.put(pos.getKey(), alpha - pos.MIN_SCORE + 1)
        ##print(f"{alpha}, depth = {depth}, col = {col}")
        return alpha, col

    # Méthode pour résoudre la position actuelle
    def solve(self, pos: Position, weak=False):
        depth = 15  # Profondeur max parcourue
        finCol = 3
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
            res, col = self.negamax(pos, med, med + 1, depth)
            if res <= med:
                max = res
            else:
                min = res
                finCol = col
        if finCol == -1:
            for x in [3, 2, 4, 1, 5, 0, 6]:
                if pos.canPlay(x):
                    finCol = x
                    break
        print("ezaeza", min, finCol)
        return min, finCol  # Retourne le score final et la colonne du meilleur coup

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
    coup_joue = "2252576253462244111563365343671351441"
    pos = Position()
    pos.initBoard(coup_joue)
    s = Negamax()
    print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
    score, best_col = s.solve(pos)
    print("Score Final:", score)
    print("Meilleur coup (colonne):", best_col)
