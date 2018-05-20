from Model.Attribute import Attribute
from Model.Inventory import Inventory


class Character:

    def __init__(self, name):
        self.name = name
        self.str = Attribute(10)
        self.con = Attribute(10)
        self.dex = Attribute(10)
        self.int = Attribute(10)
        self.wis = Attribute(10)
        self.cha = Attribute(10)
        self.inventory = Inventory()
        return
