from workplan import Workplan
from activity import Activity
from material import Material

class Recipe:

    def __init__(self):
        self.material = None # material resulting from this recipe
        self.plan = Workplan() # default workplan for this material

    def getNeededMaterials(self) -> dict[Material, int]:
        materials = dict()
        for step in self.plan.steps:
            activity : Activity = step[1]
            for material in activity.materials:
                materials[material[0] : Material] += material[1]
        return materials

    def changeWorkplan(self, plan : Workplan):
        self.plan = plan
