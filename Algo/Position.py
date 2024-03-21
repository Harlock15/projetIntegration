import numpy as np
class Position:
    """
    Classe qui gére les informations sur les positions des jetons sur le plateau
    Cette classe utilise un bitboard pour stocker l'information.
    """
    def __init__(self):
        self.WIDTH = 7
        self.HEIGHT = 6
        self.current_pos = 0
        self.mask = 0
        self.moves = 0
        self.MIN_SCORE = -(self.WIDTH*self.HEIGHT)/2 + 3

    def initPos(self, pos):
        self.current_pos = pos.current_pos
        self.mask = pos.mask
        self.moves = pos.moves

    def initBoard(self, coup_joue:str):
        for i in range(len(coup_joue)):
            col = int(coup_joue[i]) - 1
            self.play(col)


    def play(self, col:int):
        self.current_pos ^= self.mask
        next_pos = self.mask | self.mask + (1 << (col * (self.HEIGHT + 1)))
        self.mask = next_pos
        self.moves += 1

    def nbMove(self):
        return self.moves

    def canPlay(self, colonne):
        return not self.mask & (1 << ((self.HEIGHT - 1) + (colonne * (self.HEIGHT + 1))))

    def isWinningMove(self, colonne):
        pos = self.current_pos
        maskTmp = self.mask
        pos ^= maskTmp
        maskTmp |= maskTmp + (1 << (colonne * (self.HEIGHT + 1)))
        pos ^= maskTmp

        return self.checkWin(pos)

    def checkWin(self,pos):
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
        return self.mask + self.current_pos