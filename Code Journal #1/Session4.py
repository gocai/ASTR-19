class FavoriteAnimal:
    def __init__(self, arms, legs, eyes, hasTail, isFurry):
        self.arms = arms
        self.legs = legs
        self.eyes = eyes
        self.hasTail = hasTail
        self.isFurry = isFurry
    
    def CreateAnimal(self):
        print(f"Arm count: {self.arms}")
        print(f"Leg count: {self.legs}")
        print(f"Eye count: {self.eyes}")
        print(f"Has tail? {self.hasTail}")
        print(f"Is furry? {self.isFurry}")

myFavorite = FavoriteAnimal(0,4,2,True,True)
myFavorite.CreateAnimal()