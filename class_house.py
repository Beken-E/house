class House:

    def __init__(self, household_type, total_area, furniture, remaining_area = 0):
        self.household_type = household_type
        self.total_area = total_area
        self.remaining_area = remaining_area
        self.furniture = furniture
        self.square_furniture()
        


    def square_furniture(self):
        self.fur_area = 0
        for i in self.furniture.values():
            self.fur_area += i
        return self.fur_area


    def __str__(self):
        return f'Type: {self.household_type}, Total area of house: {self.total_area}, remaining area is: {self.total_area - self.fur_area}, list of furniture: {[i for i in self.furniture.keys()]}'


flat = House('Flat', 100, {'bed':4, 'wardrobe':2, 'table':1.5})

print(flat)
        