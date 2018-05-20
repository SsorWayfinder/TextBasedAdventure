import math

from Model.Levelable import Levelable


class Attribute(Levelable):

    def __init__(self, points):
        super(Attribute, self).__init__(10, points)
        return

    def __calcMod(self):
        return math.floor((self.level-10)/2)

    def used(self, amount):
        pass

    def getPoints(self):
        return self.level

    def addMod(self):
        self.used(1)
        return self.__calcMod()
