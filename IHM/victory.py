from tkinter import Toplevel, Label


class victory(Toplevel):
    def __init__(self, gagnant):
        super().__init__()
        self.title("Vainqueur")

        label = Label(self, text=f"Le joueur {gagnant} a gagné!")
        label.pack()


