import abc


class Levelable(abc.ABC):

    level: int

    def __init__(self,  start_level):
        self.level = start_level
        return

    @abc.abstractmethod
    def levelup(self, exp):
        pass


