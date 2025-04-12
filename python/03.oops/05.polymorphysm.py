class car:
    total_car = 0  # Define a class attribute to track the total number of cars

    def __init__(self, brand, model):  # __init__ => constructor
        self.brand = brand
        self.model = model
        car.total_car += 1  # Increment the total car count

    def full_name(self):  # Properly indented inside the class
        return f"{self.brand} {self.model}"


my_car = car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(car.total_car)  # Access the total car count using the class name
print(my_car.full_name())  # Call the full_name method

my_new_car = car("Tata", "Safari")
print(my_new_car.model)
print(car.total_car)  # Access the updated total car count