import time

from Algo.Negamax import Negamax
from Algo.Position import Position

class Benchmark:
    def __init__(self):
        self.nbrTotTest = 0
        self.nbrTestOk = 0
        self.moyTmp = 0
        self.tmpTot = 0
        self.nodeParcMoy = 0
        self.nodeParcTot = 0

    def testNegamax(self):
        with open("./TestFile/Test_L3_R1", 'r') as fichier:
            lignes = fichier.readlines();
            self.nbrTotTest = len(lignes)
            for i in range(self.nbrTotTest):
                ligne = lignes[i].strip().split(' ')

                scoreAtt = ligne[1]
                coup_joue = ligne[0]

                pos = Position(coup_joue)

                s = Negamax()
                start = time.time()
                scoreObt = s.negamax(pos)
                self.tmpTot += time.time() - start

                self.nodeParcTot += s.noeuds_parcourus

                if(str(scoreObt) != scoreAtt):
                    print(f"Erreur Ligne {i+1} | ScoreObt: {scoreObt} ScoreAtt: {scoreAtt}")
                else:
                    self.nbrTestOk += 1
                    print(f"{i+1}/{self.nbrTotTest} -> OK")

            self.nodeParcMoy = self.nodeParcTot/self.nbrTotTest
            self.moyTmp = self.tmpTot/self.nbrTotTest

            print(f"Test reussi: {self.nbrTestOk}/{self.nbrTotTest}")
            print(f"Moy Noeud Parcourus: {self.nodeParcMoy}")
            print(f"Tmp Moy: {self.moyTmp}")



if __name__=="__main__":
    bench = Benchmark()
    bench.testNegamax()
