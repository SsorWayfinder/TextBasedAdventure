import math

from Model.Levelable import Levelable
from Model.Character import Character


class Attribute(Levelable):

    scale = 500
    tempChange = 0

    def levelup(self, exp):
        spent = 0
        while exp > spent + self.scale*self.level:
            spent += self.scale*self.level
            self.level += 1
        return spent

    def __init__(self, points):
        super(Attribute, self).__init__(points)
        return

    def calcMod(self):
        return math.floor((self.level-10)/2)

    def getPoints(self):
        return self.level


class CarryWeight(Levelable):

    scale = 50

    def __init__(self, character: Character):
        super(Attribute, self).__init__(0)
        self.strength = character.str
        return

    def levelup(self, exp):
        spent = 0
        while exp > spent + self.scale * (self.level+self.strength):
            spent += self.scale * self.scale * (self.level+self.strength)
            self.level += 1
        return spent

    def getPoints(self):
        return self.level+self.strength


class Stamina(Levelable):

    scale = 50

    def __init__(self, character: Character):
        super(Attribute, self).__init__(0)
        self.character = character
        self.strength = character.str
        self.currentPoints = self.strength
        return

    def levelup(self, exp):
        spent = 0
        while exp > spent + self.scale * (self.level+self.strength):
            spent += self.scale * self.scale * (self.level+self.strength)
            self.level += 1
        return spent

    def getMaxPoints(self):
        return self.level+self.strength

    def spendStamina(self, pointsSpent):
        self.currentPoints -= pointsSpent
        if self.currentPoints < 0:
            self.character.str.tempChange -= pointsSpent

    def getCurrentPoints(self):
        return self.currentPoints

    def recoverStamina(self, points):
        if self.currentPoints+points > self.getMaxPoints():
            points = self.getMaxPoints() - self.currentPoints
        if self.currentPoints < 0:
            self.character.str.tempChange += points
        self.currentPoints += points

