from .thrower_dragon import ThrowerDragon
from utils import random_or_none

class ShortThrower(ThrowerDragon):
    """A ThrowerDragon that only throws stones at Terminators at most 3 places away."""

    name = 'Short'
    food_cost = 2
    def __init__(self, armor=1):
        super().__init__(armor=armor)
    
    # OVERRIDE CLASS ATTRIBUTES HERE
    max_range = 3
    min_range = 0
    # BEGIN 2.1
    implemented = False  # Change to True to view in the GUI
    def nearest_terminator(self, skynet):
        temp = self.place
        i = 0
        while temp != skynet and i <= self.max_range and i >= self.min_range:
                if temp.terminators != []:
                    return random_or_none(temp.terminators)
                else:
                    temp = temp.entrance
                    i += 1

        if temp == skynet:
            return None
    # END 2.1
