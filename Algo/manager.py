from Config import builder  # Importation de la classe Builder depuis le module Config
from Data.Case import Case  # Importation de la classe Case depuis le module Data.Case
from Data.pion import Pion  # Importation de la classe Pion depuis le module Data.pion

class Manager:
    def __init__(self):
        # Initialisation des attributs de la classe Manager
        self.plato = builder.Builder.init_plato()  # Initialisation du plateau de jeu à l'aide de la méthode init_plato de la classe Builder
        self.joueurX = builder.Builder.init_joueur('Rouge')  # Initialisation du joueur X avec la couleur 'Rouge'
        self.joueurO = builder.Builder.init_joueur('Jaune')  # Initialisation du joueur O avec la couleur 'Jaune'
        self.nbTour = 0  # Initialisation du nombre de tours à 0
        self.joueur_actuel = self.joueurX  # Initialisation du joueur actuel avec le joueur X
        self.case = None  # Initialisation de l'attribut case à None
        self.board = []
        self.fin=-1
        self.callbacks = []

    # Méthodes getters pour récupérer les joueurs

    def get_joueurX(self):
        return self.joueurX

    def get_joueurO(self):
        return self.joueurO

    # Méthodes getters et setters pour récupérer et définir le joueur actuel
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

    # Méthode pour passer au prochain tour
    def prochainTour(self):
        if self.case.get_ligne() != -1:
            self.joueur_actuel = self.joueurO if self.joueur_actuel == self.joueurX else self.joueurX

    # Méthode pour ajouter un pion dans une colonne spécifique
    def ajoutPion(self, colonne, verif):
        self.board.append(colonne + 1)


        rst = False  # Initialisation du résultat à False
        # Parcours des lignes de la colonne de bas en haut
        for ligne in range(self.plato.get_line_count() - 1, -1, -1):
            case = self.plato.get_case(colonne,ligne)  # Récupération de la case à la position (colonne, ligne)
            if case.estVide():  # Vérification si la case est vide
                nouveau_pion = Pion((ligne, colonne), self.joueur_actuel)  # Création d'un nouveau pion avec la position et le joueur actuel
                case.set_pion(nouveau_pion)  # Attribution du pion à la case
                print(f"({colonne}, {ligne})")  # Affichage de la position du nouveau pion
                self.case = case  # Mise à jour de l'attribut case avec la case où le pion a été ajouté
                rst = True  # Mise à jour du résultat à True pour indiquer qu'un pion a été ajouté
                break  # Sortie de la boucle
        if not rst:
            self.case=Case(-1,-1)  # Aucune case vide trouvée dans la colonne spécifiée
            print(f"Aucune case vide trouvée dans la colonne {colonne}")
        return rst  # Retour du résultat (True si un pion a été ajouté, False sinon)

    # Méthode pour vérifier s'il y a un gagnant après l'ajout d'un pion
    def verif(self, pion):
        row, col = pion.get_position()  # Récupération de la position du pion (ligne, colonne)

        # Vérification des pions alignés verticalement
        veri = 0
        for ii in range(self.plato.get_line_count() - 1, -1, -1):
            case = self.plato.get_case(col,ii)
            if not case.estVide() and case.get_pion().get_joueur() == self.joueur_actuel:
                veri += 1
            elif not case.estVide() and case.get_pion().get_joueur() != self.joueur_actuel:
               veri=0
        if veri >=4:
            return True

        # Vérification des pions alignés horizontalement
        veri = 0
        for ij in range(self.plato.get_column_count()):
            pion = self.plato.get_case(ij, row).get_pion()
            if pion is None:
                continue
            if pion.get_joueur() == self.joueur_actuel:
                veri = 1
            for offset in range(1, 4):
                if ij + offset >= self.plato.get_column_count():
                    break
                adjacent_pion = self.plato.get_case(ij + offset, row).get_pion()
                if adjacent_pion is None or adjacent_pion.get_joueur() != self.joueur_actuel:
                    break
                veri += 1
            if  veri >= 4:
                return True

        # Vérification des pions alignés en diagonale (de haut à gauche à bas à droite)
        veri = 0
        for i in range(-3, 4):
            x = row + i
            y = col - i
            if 0 <= x < self.plato.get_line_count() and 0 <= y < self.plato.get_column_count():
                case = self.plato.get_case(y, x)
                if not case.estVide() and case.get_pion().get_joueur() == self.joueur_actuel:
                    veri += 1
                else:
                    veri = 0
        if veri >= 4:
            return True

        # Vérification des pions alignés en diagonale (de haut à droite à bas à gauche)
        veri = 0
        for i in range(-3, 4):
            x = row - i
            y = col - i
            if 0 <= x < self.plato.get_line_count() and 0 <= y < self.plato.get_column_count():
                case = self.plato.get_case(y, x)
                if not case.estVide() and case.get_pion().get_joueur() == self.joueur_actuel:
                    veri += 1
                else:
                    veri = 0
        if veri >= 4:
            return True

        return False  # Aucune configuration gagnante trouvée

    def play(self, colonne):
        pion_ajoute = self.ajoutPion(colonne)
        if pion_ajoute:
            if self.verif(self.case.get_pion()):  # Si un pion a été ajouté et qu'il y a un gagnant
                return False  # Retourne False pour indiquer que la partie est terminée
        return True  # Retourne True pour indiquer que la partie continue

    # Méthodes getters et setters pour récupérer et définir le joueur actuel
    def get_joueurActuel(self):
        return self.joueur_actuel

    def get_case(self):
        return self.case

    def set_case(self, case):
        self.case = case

    def get_board(self):
        return self.board