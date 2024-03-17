# main.py

import tkinter as tk
from Config.Configuration import Configuration
from PIL import Image, ImageTk
from IHM.StrategyPaint import StrategyPaint
from Algo.manager import Manager
from IHM.victory import victory


class Main:
    def __init__(self):
        self.manager = Manager()
        self.strategy_paint = StrategyPaint(self.manager)
        self.active = True
        self.canvas=None
        self.root = tk.Tk()
        self.manager.add_callback(self.on_fin_changed)

    def on_fin_changed(self):
        if self.manager.get_fin() == 0:
            self.strategy_paint.effacer_pions(self.canvas, self.manager.get_plato())
            self.active = True
        elif self.manager.get_fin() == 1:
            self.root.destroy()


    def clic_souris(self, event, canvas):
        if not self.active:
            return
        x, y = event.x, event.y


        ligne = y // Configuration.BLOCK_SIZE
        colonne = x // Configuration.BLOCK_SIZE


        if 0 <= ligne < self.manager.plato.get_line_count() and 0 <= colonne < self.manager.plato.get_column_count():
            if self.manager.play(colonne) :
                self.strategy_paint.paintP(self.manager.get_case(), canvas)
                self.manager.prochainTour()
            else:
                self.strategy_paint.paintP(self.manager.get_case(), canvas)
                victory(self.manager.get_joueur_actuel().get_type(),self.manager)
                self.active = False

        else:
            print("Clic en dehors du plateau.")


    def main(self):

        self.root.title("Simple Game Board")
        self.root.attributes('-fullscreen', True)

        self.root.configure(bg='ivory')

        cell_size = Configuration.BLOCK_SIZE

        self.canvas = tk.Canvas(self.root, width=(self.manager.plato.get_column_count()+1) * cell_size,
                           height=(self.manager.plato.get_line_count()+1) * cell_size)

        self.canvas.pack()

        self.strategy_paint.paint(self.canvas, self.manager.plato)


        self.canvas.bind("<Button-1>", lambda event: self.clic_souris(event, self.canvas))

        self.root.mainloop()


