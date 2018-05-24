from Model.Attribute import *
from Model.Inventory import Inventory


class Character:

    def __init__(self, name, strength, constitution, dexterity, intelligence, wisdom, charisma):
        self.name = name
        self.str = Attribute(strength)
        self.con = Attribute(constitution)
        self.dex = Attribute(dexterity)
        self.int = Attribute(intelligence)
        self.wis = Attribute(wisdom)
        self.cha = Attribute(charisma)
        self.carryWeight = CarryWeight(self)
        self.stamina = Stamina(self)

        self.levelables = [
            self.str, self.con, self.dex, self.int, self.wis, self.cha
        ]
        self.inventory = Inventory()
        return

    def __init__(self, name):
        self.__init__(name, 10, 10, 10, 10, 10, 10)
        return
