from material import Material

class Activity:

    def __init__(self):
        self.duration = 0
        self.materials = list() # list of tuple - materials needed + amount
        self.workstations = list() # list of workstations needed to finish activity

    def __init__(self, materialList : dict, duration : int):
        self.duration = duration
        self.materials = list()
        for material in materialList.keys:
            entry = (material, materialList[material])
            self.materials.append(entry)
