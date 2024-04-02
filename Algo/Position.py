import numpy as np

class Position:
    """
    Classe qui gère les informations sur les positions des jetons sur le plateau.
    Cette classe utilise un bitboard pour stocker l'information.
    """
    def __init__(self):
        self.WIDTH = 7
        self.HEIGHT = 6
        self.current_pos = 0  # Position actuelle des jetons
        self.mask = 0  # Masque représentant les jetons sur le plateau
        self.moves = 0  # Nombre de coups joués
        self.MIN_SCORE = -(self.WIDTH*self.HEIGHT)/2 + 3  # Score minimal possible

    def initPos(self, pos):
        # Initialise la position actuelle, le masque et le nombre de coups joués
        self.current_pos = pos.current_pos
        self.mask = pos.mask
        self.moves = pos.moves

    def initBoard(self, coup_joue: str):
        # Initialise le plateau en jouant les coups donnés dans la séquence coup_joue
        for i in range(len(coup_joue)):
            col = int(coup_joue[i]) - 1
            self.play(col)

    def play(self, col: int):
        # Joue un coup dans la colonne donnée
        self.current_pos ^= self.mask
        next_pos = self.mask | self.mask + (1 << (col * (self.HEIGHT + 1)))
        self.mask = next_pos
        self.moves += 1

    def nbMove(self):
        # Renvoie le nombre de coups joués
        return self.moves

    def canPlay(self, colonne):
        # Vérifie si un coup peut être joué dans la colonne donnée
        return not self.mask & (1 << ((self.HEIGHT - 1) + (colonne * (self.HEIGHT + 1))))

    def isWinningMove(self, colonne):
        # Vérifie si jouer dans la colonne donnée conduit à une victoire
        pos = self.current_pos
        maskTmp = self.mask
        pos ^= maskTmp
        maskTmp |= maskTmp + (1 << (colonne * (self.HEIGHT + 1)))
        pos ^= maskTmp

        return self.checkWin(pos)

    def checkWin(self, pos):
        # Vérifie s'il y a une victoire dans la position donnée
        test = pos & (pos >> (self.HEIGHT + 1))
        if(test & (test >> (self.HEIGHT + 1)*2)):
            return True

        test = pos & (pos >> 8)
        if(test & (test >> 16)):
            return True

        test = pos & (pos >> 6)
        if(test & (test >> 12)):
            return True

        test = pos & (pos >> 1)
        if(test & (test >> 2)):
            return True

        return False

    def getKey(self):
        # Renvoie une clé représentant l'état actuel du jeu
        return self.mask + self.current_pos
