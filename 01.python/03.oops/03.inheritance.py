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

my_Tesla = electric_car("tesla", "model s", "85kWh")
print(my_Tesla.full_name())  # Call the full_name method from the parent class
    