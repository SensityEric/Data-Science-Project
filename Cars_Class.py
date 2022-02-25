
class Cars:
    def __init__(self, brand, number_of_doors, fuel_type):
        self.brand = brand
        self. number_of_doors = number_of_doors
        self.fuel_tpye = fuel_type

    def reverse(self):
        print(f"Hello {self.brand}, please beware")

Brand1 = Cars("Toyota", 2,"Water")


Brand1.brand = "Range Rover"
Brand1.fuel_type = "Gas"
Brand1.number_of_doors = 4

del Brand1.fuel_tpye
print(Brand1.brand,Brand1.number_of_doors)

Brand1.reverse()








