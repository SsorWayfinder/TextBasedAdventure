import math

from Model.Levelable import Levelable


class Attribute(Levelable):

    def levelup(self, exp):
        leveledUp = False
        while exp > 0:
            if exp > 500*self.level:
                exp -= 500*self.level
                self.level += 1
                leveledUp = True
            else:
                exp = -1
        return leveledUp

    def __init__(self, points):
        super(Attribute, self).__init__(points)
        return

    def calcMod(self):
        return math.floor((self.level-10)/2)

    def getPoints(self):
        return self.level
