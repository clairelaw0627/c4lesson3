class IkeaFurniture:

    def __init__(self, name, dimensions, material, price):
        self.name = name # variable, object attribute
        self.dimensions = dimensions  # dimensions should be a tuple (width, height, depth)
        self.material = material
        self.price = price

    def __str__(self):
        return(self.name)
sample = IkeaFurniture('bookcase',(80,200,10),'particle board', 199.9)
print(sample)