import math

from Model.Levelable import Levelable


class Attribute(Levelable):

    def __init__(self, points, ):
        super(Attribute, self).__init__(math.pow(1.5, points-1), points, 1.5)
        return

    def __calcMod(self):
        return math.floor((self.level-10)/2)

    def getPoints(self):
        return self.level

    def addMod(self):
        return self.__calcMod()
