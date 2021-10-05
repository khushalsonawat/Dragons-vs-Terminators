from .dragon import Dragon


class HarvesterDragon(Dragon):
    """HarvesterDragon produces 1 additional food per turn for the colony."""

    name = 'Harvester'
    implemented = True
    
    # OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 2
    def __init__(self, armor=1):
        super().__init__(armor = armor)
        

    def action(self, colony):
        """Produce 1 additional food for the colony.

        colony -- The DragonColony, used to access game state information.
        """
        colony.food += 1
        # BEGIN 1.1
        "*** YOUR CODE HERE ***"
