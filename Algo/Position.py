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
        self.MIN_SCORE = -(self.WIDTH*self.HEIGHT)//2 + 3

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

    def posNonLose(self):
        assert not self.canWinNext()
        possible_mask = self.possible()
        opponent_win = self.winningPosition(self.current_pos ^ self.mask, self.mask)
        forced_moves = possible_mask & opponent_win
        if forced_moves:
            if forced_moves & (forced_moves - 1):  # check if there is more than one forced move
                return 0  # the opponent has two winning moves and you cannot stop him
            else:
                possible_mask = forced_moves  # enforce to play the single forced move
        return possible_mask & ~(opponent_win >> 1)  # avoid playing below an opponent winning spot

    def play_sequence(self, seq):
        for move in seq:
            col = int(move) - 1
            if not (0 <= col < self.WIDTH) or not self.canPlay(col) or self.isWinningMove(col):
                break
            self.play(col)

    def canPlay(self, colonne):
        return not self.mask & (1 << ((self.HEIGHT - 1) + (colonne * (self.HEIGHT + 1))))

    def isWinningMove(self, colonne):
        return self.winningPosition(self.current_pos, self.mask) & self.possible() & (1 << ((self.HEIGHT - 1) + (colonne * (self.HEIGHT + 1))))

    def canWinNext(self):
        return self.winningPosition(self.current_pos, self.mask) & self.possible()

    def winningPosition(self, position, mask):
        # vertical
        r = (position << 1) & (position << 2) & (position << 3)

        # horizontal
        p = (position << (self.HEIGHT + 1)) & (position << (2 * (self.HEIGHT + 1)))
        r |= p & (position << (3 * (self.HEIGHT + 1)))
        r |= p & (position >> (self.HEIGHT + 1))
        p = (position >> (self.HEIGHT + 1)) & (position >> (2 * (self.HEIGHT + 1)))
        r |= p & (position << (self.HEIGHT + 1))
        r |= p & (position >> (3 * (self.HEIGHT + 1)))

        # diagonal 1
        p = (position << self.HEIGHT) & (position << (2 * self.HEIGHT))
        r |= p & (position << (3 * self.HEIGHT))
        r |= p & (position >> self.HEIGHT)
        p = (position >> self.HEIGHT) & (position >> (2 * self.HEIGHT))
        r |= p & (position << self.HEIGHT)
        r |= p & (position >> (3 * self.HEIGHT))

        # diagonal 2
        p = (position << (self.HEIGHT + 2)) & (position << (2 * (self.HEIGHT + 2)))
        r |= p & (position << (3 * (self.HEIGHT + 2)))
        r |= p & (position >> (self.HEIGHT + 2))
        p = (position >> (self.HEIGHT + 2)) & (position >> (2 * (self.HEIGHT + 2)))
        r |= p & (position << (self.HEIGHT + 2))
        r |= p & (position >> (3 * (self.HEIGHT + 2)))

        bottom_mask = self.bottom(self.WIDTH, self.HEIGHT)
        board_mask = bottom_mask * ((1 << self.HEIGHT) - 1)
        return r & (board_mask ^ mask)

    def possible(self):
        return (self.mask + self.bottom(self.HEIGHT, self.WIDTH)) & self.bottom(self.WIDTH, self.HEIGHT) * ((1 << self.HEIGHT) - 1)


    def bottom(self, width, height):
        return 0 if width == 0 else self.bottom(width-1, height) | 1 << (width-1)*(height+1)


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

    def columnMask(self, col):
        return ((1 << self.HEIGHT)-1) << col*(self.HEIGHT + 1)