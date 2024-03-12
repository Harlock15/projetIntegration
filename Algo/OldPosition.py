class Position:
    def __init__(self, coup_joue:str):
        self.WIDTH = 7
        self.HEIGHT = 6
        self.coup_joue = coup_joue
        self.board, self.height, self.moves = self.readString()

    def canPlay(self, colonne):
        return self.height[colonne] < self.HEIGHT

    def play(self, colonne):
        self.board[colonne][self.height[colonne]] = 1 + self.moves%2
        self.height[colonne] += 1
        self.moves += 1
        self.coup_joue += str(colonne+1)

    def isWinningMove(self, colonne):
        current_player = 1 + self.moves % 2
        if (self.height[colonne] >= 3 and self.board[colonne][self.height[colonne]-1] == current_player and
                self.board[colonne][self.height[colonne] - 2] == current_player and self.board[colonne][self.height[colonne] - 3] == current_player):
            return True

        for i in range(-1, 2):
            nb = 0
            for ii in [-1, 1]:
                x = colonne + ii
                y = self.height[colonne] + i*ii
                while 0 <= x < self.WIDTH and 0 <= y < self.HEIGHT and self.board[x][y] == current_player:
                    nb += 1
                    x += ii
                    y += i*ii
            if nb >= 3:
                return True
        return False

    def nbMove(self):
        return self.moves

    def affBoard(self):
        for j in range(5,-1,-1):
            for i in range(7):
                print(self.board[i][j], end="|")
            print("")

    def readString(self):
        move = len(self.coup_joue)  # Le nombre de coup joue
        height = [0, 0, 0, 0, 0, 0, 0]  # Le nombre de jeton par colonne
        board = [[0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]]     # 0 si rien n'a été jouer dans cette emplacement
        # 1 si le premier a avoir jouer possède le pions jouer et
        # 2 si c'est l'autre joueur
        for i in range(len(self.coup_joue)):
            board[int(self.coup_joue[i])-1][height[int(self.coup_joue[i])-1]] = 1 + i % 2
            height[int(self.coup_joue[i]) - 1] += 1

        return board, height, move


if __name__ == "__main__":
    coup_joue = "313131"
    pos = Position(coup_joue)
    pos.affBoard()
    print(pos.isWinningMove(3))
    print(pos.canPlay(3))
    pos.play(3)

    pos.play(3)
    pos.play(3)
    pos.affBoard()
    print(pos.canPlay(3))
