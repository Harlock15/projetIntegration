from Plateau import Plateau
from Configuration import Configuration

class Builder:
    @staticmethod
    def init_plato():
        return Plateau(Configuration.LINE_COUNT, Configuration.COLUMN_COUNT)

