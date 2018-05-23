from typing import List

from Model.Item import Item


class Inventory:

    items: List[Item]

    def __init__(self):
        self.items = []
        return

    def getTotalWeight(self):
        weight = 0.0
        for item in self.items:
            weight += item.weight

        return weight
