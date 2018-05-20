import abc


class Levelable:

    #TODO: change to be more like grpg9k's xp spending system.

    def __init__(self, scale, start_level):
        self.__init__(scale, start_level, 2)
        return

    def __init__(self, scale, start_level, growth):
        self.scaling = scale
        self.experience = 0
        self.start_level = start_level
        self.growth = growth
        return

    @abc.abstractmethod
    def used(self, amount):
        old_level = self.level
        self.experience += amount
        current_level = self.level

        if current_level > old_level:
            return True

        return False

    @property
    def level(self):
        current_level = self.start_level
        xp = self.experience
        scale = self.scaling
        growth = self.growth

        xp -= scale
        scale *= growth
        while xp > 0:
            current_level += 1
            xp -= scale
            scale *= growth

        return current_level
