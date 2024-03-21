import os
from tkinter import *

from PIL import Image, ImageTk


from IHM.StrategyPaint import StrategyPaint
from Algo.manager import Manager

from IHM.main import Main


class Accueil:
    def __init__(self):
        self.gui = Tk()
        self.gui.attributes('-fullscreen', True)


        self.manager = Manager()
        self.strategy_paint = StrategyPaint(self.manager)


        canvas = Canvas(self.gui, width=self.gui.winfo_screenwidth(), height=self.gui.winfo_screenheight())
        canvas.pack(expand=YES, fill=BOTH)

        label = Label(canvas)
        label.pack(pady=150)

        image = Image.open("image/bg1.png")

        # Convertir l'image pour l'afficher avec Tkinter
        photo = ImageTk.PhotoImage(image)

        # Afficher l'image sur le canevas
        canvas.create_image(0, 0, image=photo, anchor=NW)




        self.btn1 = Button(canvas, text="commencer ", font=10, command=self.jeu,padx = 32,
  pady = 20)
        self.btn2 = Button(canvas, text="quitter", font=10, command=self.gui.destroy, padx=32, pady=20)
        # Utilise la gestion de géométrie pack pour centrer les boutons
        self.btn1.pack(side=LEFT, padx=300)
        self.btn2.pack(side=LEFT, padx=100)

        self.gui.mainloop()

    def jeu(self):

        self.gui.destroy()
        main_instance = Main()

        main_instance.main()


if __name__ == "__main__":
    accueil = Accueil()
