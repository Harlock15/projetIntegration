import datetime
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
        fichtest = ["Test_L3_R1","Test_L2_R1","Test_L2_R2","Test_L1_R1","Test_L1_R2","Test_L1_R3"]
        for i in fichtest:
            self.testNegamaxFich(i)


    def testNegamaxFich(self, fich):
        with open(f"./result", "w") as res:
            res.write(f"[{datetime.datetime.now()}]\n")
            self.nbrTotTest = 0
            self.tmpTot = 0
            self.nodeParcTot = 0
            self.nbrTestOk = 0
            with open(f"./TestFile/{fich}", 'r') as fichier:
                lignes = fichier.readlines()
                self.nbrTotTest = len(lignes)
                for x in range(self.nbrTotTest):
                    ligne = lignes[x].strip().split(' ')

                    scoreAtt = ligne[1]
                    coup_joue = ligne[0]

                    pos = Position(coup_joue)

                    s = Negamax()
                    start = time.time()
                    weak = False
                    scoreObt = s.solve(pos)
                    self.tmpTot += time.time() - start

                    self.nodeParcTot += s.noeuds_parcourus
                    if (str(scoreObt) != scoreAtt):
                        res.write(f"[{datetime.datetime.now()}] [{fich}] Erreur Ligne {x + 1} | ScoreObt: {scoreObt} ScoreAtt: {scoreAtt}\n")
                    else:
                        if((x+1)%100 == 0):
                            print(f"Test {x + 1}: OK")
                        self.nbrTestOk += 1

                self.nodeParcMoy = self.nodeParcTot / self.nbrTotTest
                self.moyTmp = self.tmpTot / self.nbrTotTest


                print(f"----------\nFichier {fich}\nTest reussi: {self.nbrTestOk}/{self.nbrTotTest}\nMoy Noeud Parcourus: {self.nodeParcMoy}\nTmp Moy: {self.moyTmp}\n----------")
                res.write(f"----------\n[{datetime.datetime.now()}]\nFichier {fich}\nTest reussi: {self.nbrTestOk}/{self.nbrTotTest}\nMoy Noeud Parcourus: {self.nodeParcMoy}\nTmp Moy: {self.moyTmp}\n----------")




if __name__ == "__main__":
    bench = Benchmark()
    bench.testNegamaxFich("Test_L3_R1")
