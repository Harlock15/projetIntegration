import tkinter as tk

import Configuration
from Plateau import *
from builder import Builder


class GameBoard:
    def __init__(self, root,plato):
        self.root = root
        self.rows = plato.get_line_count()
        self.columns = plato.get_column_count()
        self.cell_size = Configuration.Configuration.BLOCK_SIZE
        self.cases = plato.get_cases()
        self.canvas = tk.Canvas(root, width=self.columns * self.cell_size, height=self.rows * self.cell_size)
        self.canvas.pack()
        self.paint()

    def paint(self):

        for row in range(self.rows):
            for col in range(self.columns):
                case = self.cases[row][col]
                x1, y1 = col * self.cell_size, (row)* self.cell_size
                x2, y2 = x1 + self.cell_size,self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2,)
                self.canvas.create_oval(
                    case.get_colonne() * self.cell_size, case.get_ligne() * self.cell_size,
                    (case.get_colonne() + 1) * self.cell_size, (case.get_ligne() -1) * self.cell_size,
                    fill="white"
                )





def main():
    root = tk.Tk()
    root.title("Simple Game Board")
    root.attributes('-fullscreen', True)
    plato = Builder.init_plato()

    game_board = GameBoard(root, plato)

    root.mainloop()

if __name__ == "__main__":
    main()





