from IHM.Plateau import Plateau
from Config.Configuration import Configuration

class Builder:
    @staticmethod
    def init_plato():
        return Plateau(Configuration.LINE_COUNT, Configuration.COLUMN_COUNT)

