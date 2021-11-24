resourcePools = list()

class ResourcePool:

    def __init__(self):
        self.id = ''
        self.name = ''
        self.resources = list() # list of resources available in this resource pool
        resourcePools.append(self) # register itself to the available resource pools