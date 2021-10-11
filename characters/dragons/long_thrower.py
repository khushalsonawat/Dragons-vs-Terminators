from .thrower_dragon import ThrowerDragon
from utils import random_or_none

class LongThrower(ThrowerDragon):
    """A ThrowerDragon that only throws stones at Terminators at least 5 places away."""

    name = 'Long'
    food_cost = 2
    def __init__(self, armor=1):
        super().__init__(armor=armor)
    # OVERRIDE CLASS ATTRIBUTES HERE

    min_range = 5
    max_range = float('inf')
    # BEGIN 2.1
    implemented = False  # Change to True to view in the GUI
    def nearest_terminator(self, skynet):
        temp = self.place
        i = 0
        while i < self.min_range:
            temp = temp.entrance
            i += 1

        while temp != skynet:
            if i < self.max_range:
                if temp.terminators != []:
                    return random_or_none(temp.terminators)
                else:
                    temp = temp.entrance

        if temp == skynet:
            return None
    # END 2.1
