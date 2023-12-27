import IHM.StrategyPaint as StrategyPaint


class display:
    def __init__(self,plato,mana):
        self.plato=plato
        self.mana=mana

    def painCompenent(self):
        StrategyPaint.paint(self.plato)