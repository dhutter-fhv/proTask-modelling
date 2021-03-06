from activity import Activity
from material import Material

class Recipe:

    def __init__(self):
        self.id = ''
        self.material = None # material resulting from this recipe
        self.plan = list() # default workplan for this material (list of activities)

    def getNeededMaterials(self) -> dict[Material, int]:
        materials = dict()
        """
            the steps in the workplan is a list of tuples [timestep, activity]
            which has the timestep [0] and the activity [1] that needs to be done
            in sequence (if multiple activities have the same timestep value, they
            could be done in parallel)
        """
        for activity in self.plan.steps:
            """
                the materials in activity is a list of tuples [material, amount]
                which hold the information which material [0] is needed in which
                quantity [1]
            """
            for material in activity.materials:
                materials[material[0] : Material] += material[1]
        return materials
