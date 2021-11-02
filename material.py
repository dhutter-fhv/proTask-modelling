from workplan import Workplan
from material import Material

class Material:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.minAmount = 0 # Losgröße
        self.versions = list() # list of alternative recipes - base material if list is empty
        self.subMaterials = list() # list of materials necessary to make this material - base material if list is empty

    def getBaseMaterials(self) -> list:
        materials = list()
        if (len(self.subMaterials)) > 0:
            for material in self.subMaterials:
                sub : list = material.getBaseMaterials()
                for s in sub: # this is just to make sure each base material only appears once in the list
                    if s not in materials:
                        materials.append(s) 
        else:
            materials.append(self)
        return materials