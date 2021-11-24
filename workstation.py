from machine import Machine
from resourcepool import ResourcePool
class Workstation:

    def __init__(self):
        self.id = ''
        self.preparationTime = 0 # time needed for the workstation to be ready
        self.dismantleTime = 0 # time needed after the work is done

        self.resources = list() # list of tuple: resource pools and lists of resources
        self.schedule = None # schedule of the workstation

    def get_needed_resources(self):
        possible_resources = list()
        for pool in self.resources:
            for needed_resource in pool[1]:
                found = False
                for available_resource in pool[0].get_resources():
                    if needed_resource == available_resource:
                        found = True
                        possible_resources.append(available_resource)
                        break
                if not found:
                    return None # return none if a resource is not available
        return possible_resources
