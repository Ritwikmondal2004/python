class car:
    def __init__(self, brand, model):  # __init__ => constructor
        self.brand = brand
        self.model = model

    def full_name(self):  # Properly indented inside the class
        return f"{self.brand} {self.model}"


my_car = car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())  # Call the full_name method
my_new_car = car("Tata", "Safari")
print(my_new_car.model)