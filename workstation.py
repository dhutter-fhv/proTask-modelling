from machine import Machine

class Workstation:

    def __init__(self):
        self.preparationTime = 0 # time needed for the workstation to be ready
        self.machines = list() # list of machines attached to the workstation
        """
            the person count in the class persons is only necessary if
            there are workstations with no machine which need human
            workers to operate
        """
        self.persons = 0 # persons necessary to operate workstation
        self.schedule = list() # list of scheduled working hours (timespans)

    def getNeededPersonsForMachines(self) -> int:
        persons = 0
        for machine in self.machines:
            persons += machine.personsNeeded
        return persons