from workplan import Workplan
from material import Material

class Material:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.minAmount = 0 # Losgröße
        self.versions = list() # list of alternative recipes
        self.subMaterials = list() # list of materials necessary to make this material - base material if list is empty
