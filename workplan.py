from activity import Activity

class Workplan:

    def __init__(self):
        self.steps = list() # list of tuple (timestep + activity connected to it)
    
    def __init__(self, steps : list):
        self.steps = steps

    def addStep(self, timestep : int, activity : Activity):
        self.steps.append((timestep, activity))

