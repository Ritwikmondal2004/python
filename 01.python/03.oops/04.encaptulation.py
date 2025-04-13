class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):  # Properly indented inside the class
        return f"{self.brand} {self.model}"

class electric_car(Car):
    def __init__(self, brand, model, battery_size):  # Fixed typo in method name
        super().__init__(brand, model)
        self.battery_size = battery_size

    def get_brand(self):  # Properly indented inside the electric_car class
        return self.brand + "!"

my_Tesla = electric_car("tesla", "model s", "85kWh")
print(my_Tesla.brand)
print(my_Tesla.get_brand())