from Config import builder
from Data.Case import Case

from Data.pion import Pion


class Manager:
    def __init__(self):
        self.plato = builder.Builder.init_plato()
        self.joueurX= builder.Builder.init_joueur('X')
        self.joueurO= builder.Builder.init_joueur('O')
        self.nbTour = 0
        self.joueur_actuel = self.joueurX
        self.case=None



    def get_joueurX(self):
        return self.joueurX


    def get_joueurO(self):
        return self.joueurO

    def get_joueur_actuel(self):
        return self.joueur_actuel

    def set_joueur_actuel(self, joueur):
        self.joueur_actuel = joueur

    def prochainTour(self):
        self.joueur_actuel = self.joueurO if self.joueur_actuel == self.joueurX else self.joueurX

    def ajoutPion(self, colonne):
        rst = False
        for ligne in range(self.plato.get_line_count() - 1, -1, -1):
            case = self.plato.get_case(colonne,ligne)
            if case.estVide():
                nouveau_pion = Pion((ligne,colonne), self.joueur_actuel)
                case.set_pion(nouveau_pion)
                print(f"({colonne}, {ligne})")
                self.case = case
                rst = True
                break

        if not rst:
            print(f"Aucune case vide trouvée dans la colonne {colonne}")

        return rst

    def verif(self, pion):

        row, col = pion.get_position()

        veri = 0
        for ii in range(self.plato.get_line_count() - 1, -1, -1):
            case = self.plato.get_case(col,ii)

            if not case.estVide() and case.get_pion().get_joueur() == self.joueur_actuel:
                veri += 1

        if veri ==4:
            return True

        veri = 0

        for ij in range(self.plato.get_column_count()):
            case = self.plato.get_case(ij, row)

            if not case.estVide() and case.get_pion().get_joueur() == self.joueur_actuel:
                veri += 1

            elif not case.estVide() and case.get_pion().get_joueur() != self.joueur_actuel:
               veri=0

        if veri == 4:
             return True

        veri = 0
        for i in range(-3, 4):
             x = row + i
             y = col - i
             if 0 <= x < self.plato.get_line_count() and 0 <= y < self.plato.get_column_count():
                 case = self.plato.get_case(y, x)
                 if not case.estVide() and case.get_pion().get_joueur() == self.joueur_actuel:
                     veri += 1
                 elif not case.estVide() and case.get_pion().get_joueur() != self.joueur_actuel:
                     veri = 0

        if veri == 4:
             return True

        veri = 0
        for i in range(-3, 4):
            a = row - i
            b = col - i
            if 0 <= a < self.plato.get_line_count() and 0 <= b < self.plato.get_column_count():
                case = self.plato.get_case(b, a)
                if not case.estVide() and case.get_pion().get_joueur() == self.joueur_actuel:
                    veri += 1
                elif not case.estVide() and case.get_pion().get_joueur() != self.joueur_actuel:
                    veri = 0

        if veri == 4:
            return True

        return False



    def play(self, colonne):

        pion_ajoute = self.ajoutPion(colonne)

        if pion_ajoute:
            if self.verif(self.case.get_pion()):
                return False
        return True
    def get_joueurActuel(self):
        return self.joueur_actuel
    def get_case(self):
        return self.case
    def set_case(self,case):
        self.case=case