import abc


class Levelable:

    def __init__(self, scale, start_level):
        self.scaling = scale
        self.experience = 0
        self.start_level = start_level
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

        xp -= scale
        scale *= 2
        while xp > 0:
            current_level += 1
            xp -= scale
            scale *= 2

        return current_level
