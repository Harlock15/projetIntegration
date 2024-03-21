from Config import builder
from Data.Case import Case

from Data.pion import Pion


class Manager:
    def __init__(self):
        self.plato = builder.Builder.init_plato()
        self.joueurX= builder.Builder.init_joueur('Rouge')
        self.joueurO= builder.Builder.init_joueur('Jaune')
        self.nbTour = 0
        self.joueur_actuel = self.joueurX
        self.case=None
        self.fin=-1
        self.callbacks = []



    def get_joueurX(self):
        return self.joueurX


    def get_joueurO(self):
        return self.joueurO

    def get_joueur_actuel(self):
        return self.joueur_actuel
    def get_plato(self):
        return self.plato

    def get_fin(self):
        return self.fin

    def set_fin(self, value):
        self.fin = value
        for callback in self.callbacks:
            callback()

    def add_callback(self, callback):
        self.callbacks.append(callback)
    def set_joueur_actuel(self, joueur):
        self.joueur_actuel = joueur

    def prochainTour(self):
        if self.case.get_ligne() != -1:
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
            self.case=Case(-1,-1)
            print(f"Aucune case vide trouvée dans la colonne {colonne}")

        return rst

    def verif(self, pion):

        row, col = pion.get_position()

        # Initialiser le compteur de pions alignés verticalement
        veri = 1  # On commence avec le pion lui-même déjà compté

        # Vérifier les pions en dessous du pion actuel dans la même colonne
        for i in range(row + 1, self.plato.get_line_count()):
            case = self.plato.get_case(col, i)
            if not case.estVide() and case.get_pion().get_joueur() == self.joueur_actuel:
                # Si la case contient un pion du même joueur, incrémentez le compteur
                veri += 1
            else:
                # Si la case est vide ou contient un pion d'un autre joueur, arrêtez la vérification
                break

        # Vérifier les pions au-dessus du pion actuel dans la même colonne
        for i in range(row - 1, -1, -1):
            case = self.plato.get_case(col, i)

            if not case.estVide() and case.get_pion().get_joueur() == self.joueur_actuel:
                # Si la case contient un pion du même joueur, incrémentez le compteur
                veri += 1
            else:
                # Si la case est vide ou contient un pion d'un autre joueur, arrêtez la vérification
                break

        # Vérifier si le nombre de pions alignés est supérieur ou égal à 4
        if veri >= 4:
            print("vertical")
            return True

        veri = 1  # On commence avec le pion lui-même déjà compté


        for i in range(col + 1,self.plato.get_column_count()):
            case = self.plato.get_case(i,row)

            if not case.estVide() and case.get_pion().get_joueur() == self.joueur_actuel:
                # Si la case contient un pion du même joueur, incrémentez le compteur
                veri += 1
            else:
                # Si la case est vide ou contient un pion d'un autre joueur, arrêtez la vérification
                break

        for i in range(col - 1, -1, -1):
            case = self.plato.get_case(i,row)

            if not case.estVide() and case.get_pion().get_joueur() == self.joueur_actuel:

                # Si la case contient un pion du même joueur, incrémentez le compteur
                veri += 1
            else:
                # Si la case est vide ou contient un pion d'un autre joueur, arrêtez la vérification
                break

        # Vérifier si le nombre de pions alignés est supérieur ou égal à 4
        if veri >= 4:
            print("horizontal")
            return True
        veri = 1  # On commence avec le pion lui-même déjà compté

        # Vérifier la diagonale en bas à droite du pion actuel
        i, j = row + 1, col + 1
        while i < self.plato.get_line_count() and j < self.plato.get_column_count():
            case = self.plato.get_case(j, i)
            if not case.estVide() and case.get_pion().get_joueur() == self.joueur_actuel:
                veri += 1
            else:
                break
            i += 1
            j += 1

        # Vérifier la diagonale en haut à gauche du pion actuel
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            case = self.plato.get_case(j, i)
            if not case.estVide() and case.get_pion().get_joueur() == self.joueur_actuel:
                veri += 1
            else:
                break
            i -= 1
            j -= 1

        # Vérifier si le nombre de pions alignés est supérieur ou égal à 4
        if veri >= 4:
            print("Diagonale bas-droite et haut-gauche")
            return True

        veri = 1  # Réinitialiser le compteur

        # Vérifier la diagonale en bas à gauche du pion actuel
        i, j = row + 1, col - 1
        while i < self.plato.get_line_count() and j >= 0:
            case = self.plato.get_case(j, i)
            if not case.estVide() and case.get_pion().get_joueur() == self.joueur_actuel:
                veri += 1
            else:
                break
            i += 1
            j -= 1

        # Vérifier la diagonale en haut à droite du pion actuel
        i, j = row - 1, col + 1
        while i >= 0 and j < self.plato.get_column_count():
            case = self.plato.get_case(j, i)
            if not case.estVide() and case.get_pion().get_joueur() == self.joueur_actuel:
                veri += 1
            else:
                break
            i -= 1
            j += 1

        # Vérifier si le nombre de pions alignés est supérieur ou égal à 4
        if veri >= 4:
            print("Diagonale bas-gauche et haut-droite")
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