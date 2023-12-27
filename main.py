import tkinter as tk

from IHM.StrategyPaint import GameBoard
from IHM.builder import Builder


def main():
    root = tk.Tk()
    root.title("Simple Game Board")
    root.attributes('-fullscreen', True)
    plato = Builder.init_plato()

    game_board = GameBoard(root, plato)

    root.mainloop()

if __name__ == "__main__":
    main()