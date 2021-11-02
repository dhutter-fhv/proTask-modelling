class Person:

    def __init__(self):
        self.machines = list() # list of machines which can be operated by this person
        self.schedule = list() # list of tuple of scheduled assignments to workplaces for timespan