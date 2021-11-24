from material import Material

class Activity:

    def __init__(self):
        self.id = '' # necessary?
        self.minOutput = 0
        self.maxOutput = 0
        self.materials = list() # list of tuple - materials needed + amount
        self.workstations = list() # list of workstations needed to finish activity
        self.machineTime = 0 # time needed for machines to run
        self.personTime = 0 # time needed for persons to work
