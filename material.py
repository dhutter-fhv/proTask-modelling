from recipe import Recipe

class Material:

    def __init__(self):
        self.id = ''
        self.name = ''
        self.minAmount = 0 # Losgröße
        self.versions = list() # list of alternative recipes - base material if list is empty
        self.isEndProduct = False
        self.stock = 0 # how much stock exists already
