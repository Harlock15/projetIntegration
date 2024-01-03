from Config import builder
from Data.pion import pion


class Manager:
    def __init__(self):
        self.plato = builder.Builder.init_plato()
        self.joueurX= builder.Builder.init_joueur('X')
        self.joueurO= builder.Builder.init_joueur('O')
        self.pionG = []
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
        for ligne in range(self.plato.get_line_count() - 1, -1, -1):
            case = self.plato.get_case(colonne, ligne)
            if case.estVide():
                # Créer une instance de la classe Pion avec les bonnes valeurs
                nouveau_pion = pion((ligne, colonne), self.joueur_actuel)
                case.set_pion(nouveau_pion)
                self.case = case
                self.joueur_actuel.get_pions().append(nouveau_pion)

                if self.verif(colonne
                              ):
                    print(f"Le joueur {self.joueur_actuel.get_type()} a gagné !")
                    # Ajoutez ici toute autre logique pour terminer la partie
                    # Peut-être réinitialiser le plateau, demander si les joueurs veulent rejouer, etc.
                    return True  # Indiquer que l'ajout de pion a réussi

                self.prochainTour()
                return True  # Indiquer que l'ajout de pion a réussi

        print(f"Aucune case vide trouvée dans la colonne {colonne}")
        return False  # Indiquer que l'ajout de pion a échoué

    def verif(self, column):
        ligne = self.get_last_pion_line(column)

        # Vérification horizontale
        for col in range(max(0, column - 3), min(self.plato.get_column_count() - 2, column + 1)):
            cases = [self.plato.get_case(ligne, col + i) for i in range(4)]
            if all(case and case.get_pion() and case.get_pion().get_joueur() == self.joueur_actuel.get_type() for case
                   in cases):
                return True

        # Vérification verticale
        for row in range(max(0, ligne - 3), min(self.plato.get_line_count() - 2, ligne + 1)):
            cases = [self.plato.get_case(row + i, column) for i in range(4)]
            if all(case and case.get_pion() and case.get_pion().get_joueur() == self.joueur_actuel.get_type() for case
                   in cases):
                return True

        # Vérification diagonale (de haut à gauche à bas à droite)
        for i in range(min(column, ligne, 3), min(column + 1, ligne + 1)):
            cases = [self.plato.get_case(ligne - i + j, column - i + j) for j in range(4)]
            if all(case and case.get_pion() and case.get_pion().get_joueur() == self.joueur_actuel.get_type() for case
                   in cases):
                return True

        # Vérification diagonale (de haut à droite à bas à gauche)
        for i in range(min(column, self.plato.get_line_count() - 1 - ligne, 3),
                       min(column + 1, self.plato.get_line_count() - ligne)):
            cases = [self.plato.get_case(ligne + i - j, column - i + j) for j in range(4)]
            if all(case and case.get_pion() and case.get_pion().get_joueur() == self.joueur_actuel.get_type() for case
                   in cases):
                return True

        # Aucune victoire détectée
        return False

    def get_last_pion_line(self, column):
        # Retourner la ligne de la dernière case vide dans la colonne
        for ligne in range(self.plato.get_line_count() - 1, -1, -1):
            if self.plato.get_case(ligne, column).estVide():
                return ligne
        return -1

    def get_joueurActuel(self):
        return self.joueur_actuel
    def get_case(self):
        return self.case
    def set_case(self,case):
        self.case=case