from PositionFunction_General import Position_general as PG
from PositionFunction_Specific import Position_catBound as PC

class Position():
    def __init__(self):
        self.PG = PG()
        self.PC = PC()

    def parseData(self, accuracy, RT, stimuli):
        self.PG.calcAccRT(accuracy, RT, stimuli)
        self.PC.calcAccRT(accuracy, RT, stimuli)