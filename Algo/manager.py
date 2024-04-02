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
        self.board = []  # Initialisation de la liste des coups joués
        self.fin = -1  # Initialisation de l'attribut indiquant la fin de la partie
        self.callbacks = []  # Initialisation de la liste des fonctions de rappel pour les mises à jour de fin de partie

    def reinitBoard(self):
        self.board = []  # Réinitialisation de la liste des coups joués

    # Méthodes getters pour récupérer les joueurs
    def get_joueurX(self):
        return self.joueurX

    def get_joueurO(self):
        return self.joueurO

    # Méthodes getters et setters pour récupérer et définir le joueur actuel
    def get_joueur_actuel(self):
        return self.joueur_actuel

    def set_joueur_actuel(self, joueur):
        self.joueur_actuel = joueur

    # Méthode pour récupérer le plateau de jeu
    def get_plato(self):
        return self.plato

    # Méthode pour récupérer l'état de fin de la partie
    def get_fin(self):
        return self.fin

    # Méthode pour définir l'état de fin de la partie
    def set_fin(self, value):
        self.fin = value
        # Appel des fonctions de rappel en cas de mise à jour de l'état de fin de partie
        for callback in self.callbacks:
            callback()
        # Réinitialisation de la liste des coups joués
        self.reinitBoard()

    # Méthode pour ajouter une fonction de rappel
    def add_callback(self, callback):
        self.callbacks.append(callback)

    # Méthode pour passer au prochain tour
    def prochainTour(self):
        if self.case.get_ligne() != -1:
            # Changement du joueur actuel
            self.joueur_actuel = self.joueurO if self.joueur_actuel == self.joueurX else self.joueurX

    # Méthode pour ajouter un pion dans une colonne spécifique
    def ajoutPion(self, colonne):
        self.board.append(colonne + 1)  # Ajout de la colonne dans la liste des coups joués

        rst = False  # Initialisation du résultat à False
        # Parcours des lignes de la colonne de bas en haut
        for ligne in range(self.plato.get_line_count() - 1, -1, -1):
            case = self.plato.get_case(colonne, ligne)  # Récupération de la case à la position (colonne, ligne)
            if case.estVide():  # Vérification si la case est vide
                nouveau_pion = Pion((ligne, colonne), self.joueur_actuel)  # Création d'un nouveau pion
                case.set_pion(nouveau_pion)  # Attribution du pion à la case
                self.case = case  # Mise à jour de l'attribut case avec la case où le pion a été ajouté
                rst = True  # Mise à jour du résultat à True pour indiquer qu'un pion a été ajouté
                break  # Sortie de la boucle
        if not rst:
            self.case = Case(-1, -1)  #
