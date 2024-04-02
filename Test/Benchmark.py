import datetime
import time

from Algo.Negamax import Negamax  # Importation de la classe Negamax depuis le module Algo.Negamax
from Algo.Position import Position  # Importation de la classe Position depuis le module Algo.Position

class Benchmark:
    def __init__(self):
        # Initialisation des variables de suivi des performances
        self.nbrTotTest = 0  # Nombre total de tests effectués
        self.nbrTestOk = 0  # Nombre de tests réussis
        self.moyTmp = 0  # Temps moyen par test
        self.tmpTot = 0  # Temps total passé pour tous les tests
        self.nodeParcMoy = 0  # Nombre moyen de nœuds parcourus par test
        self.nodeParcTot = 0  # Nombre total de nœuds parcourus

    def testNegamax(self):
        # Liste des fichiers de test à utiliser
        fichtest = ["Test_L3_R1","Test_L2_R1","Test_L2_R2","Test_L1_R1","Test_L1_R2","Test_L1_R3"]
        for i in fichtest:
            self.testNegamaxFich(i)

    def testNegamaxFich(self, fich):
        # Ouvre un fichier de résultat pour écrire les performances
        with open(f"./result_{fich}", "w") as res:
            res.write(f"[{datetime.datetime.now()}]\n")  # Écriture de la date et l'heure actuelle
            self.nbrTotTest = 0  # Réinitialisation du nombre total de tests
            self.tmpTot = 0  # Réinitialisation du temps total
            self.nodeParcTot = 0  # Réinitialisation du nombre total de nœuds parcourus
            self.nbrTestOk = 0  # Réinitialisation du nombre de tests réussis
            # Ouvre le fichier de test correspondant
            with open(f"./TestFile/{fich}", 'r') as fichier:
                lignes = fichier.readlines()  # Lecture des lignes du fichier
                self.nbrTotTest = len(lignes)  # Détermine le nombre total de tests à partir du nombre de lignes
                for x in range(self.nbrTotTest):
                    ligne = lignes[x].strip().split(' ')  # Divise la ligne en colonnes séparées par un espace

                    scoreAtt = ligne[1]  # Score attendu pour le test
                    coup_joue = ligne[0]  # Coup joué dans la position initiale

                    pos = Position()  # Crée une instance de la classe Position
                    pos.initBoard(coup_joue)  # Initialise le plateau avec le coup joué

                    s = Negamax()  # Crée une instance de la classe Negamax
                    start = time.time()  # Enregistre le temps de début du test
                    weak = False  # Détermine si l'algorithme doit être exécuté en mode faible
                    scoreObt = int(s.solve(pos))  # Obtient le score retourné par l'algorithme
                    self.tmpTot += time.time() - start  # Calcule le temps écoulé pendant le test

                    self.nodeParcTot += s.noeuds_parcourus  # Ajoute le nombre de nœuds parcourus pour ce test
                    # Vérifie si le score obtenu correspond au score attendu
                    if (str(scoreObt) != scoreAtt):
                        # Si non, écrit une erreur dans le fichier de résultats
                        res.write(f"[{datetime.datetime.now()}] [{fich}] Erreur Ligne {x + 1} | ScoreObt: {scoreObt} ScoreAtt: {scoreAtt}\n")
                    else:
                        if((x+1)%10 == 0):
                            # Affiche un message de confirmation tous les 10 tests
                            print(f"Test {x + 1}: OK")
                        self.nbrTestOk += 1  # Incrémente le nombre de tests réussis

                self.nodeParcMoy = self.nodeParcTot / self.nbrTotTest  # Calcule le nombre moyen de nœuds parcourus par test
                self.moyTmp = self.tmpTot / self.nbrTotTest  # Calcule le temps moyen par test

                # Affiche les résultats du benchmark
                print(f"----------\nFichier {fich}\nTest reussi: {self.nbrTestOk}/{self.nbrTotTest}\nMoy Noeud Parcourus: {self.nodeParcMoy}\nTmp Moy: {self.moyTmp}\n----------")
                # Écrit les résultats dans le fichier de résultats
                res.write(f"----------\n[{datetime.datetime.now()}]\nFichier {fich}\nTest reussi: {self.nbrTestOk}/{self.nbrTotTest}\nMoy Noeud Parcourus: {self.nodeParcMoy}\nTmp Moy: {self.moyTmp}\n----------")

if __name__ == "__main__":
    bench = Benchmark()  # Crée une instance de la classe Benchmark
    bench.testNegamax()  # Exécute les tests de l'algorithme Negamax
