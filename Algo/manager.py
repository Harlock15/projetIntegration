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
            case = self.plato.get_case(colonne,ligne)
            if case.estVide():
                # Créer une instance de la classe Pion avec les bonnes valeurs
                nouveau_pion = pion((ligne, colonne), self.joueur_actuel)
                case.set_pion(nouveau_pion)
                self.case=case
                self.joueur_actuel.get_pions().append(nouveau_pion)

                if not self.verif(self.joueur_actuel.get_pions(), nouveau_pion):
                    self.prochainTour()
                    return True  # Indiquer que l'ajout de pion a réussi
                else:
                    print(f"Fin")

        print(f"Aucune case vide trouvée dans la colonne {colonne}")
        return False  # Indiquer que l'ajout de pion a échoué

    def verif(self, liste_pion, pionAct):
        x, y = pionAct.get_position()

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue

                count = 1  # Commencez le compteur à 1 pour inclure le pion actuel
                new_x, new_y = x + dx, y + dy

                # Vérifier si les nouvelles coordonnées sont valides
                if 0 <= new_x < self.plato.get_line_count() and 0 <= new_y < self.plato.get_column_count():
                    caseDest = self.plato.get_case(new_x, new_y)

                    # Vérifier si la case correspond à une position existante
                    if caseDest and caseDest.get_pion() in liste_pion:
                        count += 1
                        if count >= 4:
                            return True
                    else:
                        break

        return False

    def get_joueurActuel(self):
        return self.joueur_actuel
    def get_case(self):
        return self.case
    def set_case(self,case):
        self.case=case