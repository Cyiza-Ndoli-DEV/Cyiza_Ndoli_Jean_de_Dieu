class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year, no_of_doors):
        super().__init__(make, model, year)
        self.no_of_doors = no_of_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.no_of_doors}")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike

    def display_info(self):
        super().display_info()
        print(f"Type of Bike: {self.type_of_bike}")


def display_vehicle_info(vehicles):
    for vehicle in vehicles:
        vehicle.display_info()
        print("-" * 20)


# Create vehicle objects
vehicles = [
    Car("Honda", "Civic", 2020, 4),
    Motorcycle("Yamaha", "R6", 2018, "Sport"),
    Car("Toyota", "Camry", 2022, 4),
    Motorcycle("Harley Davidson", "Street Glide", 2019, "Cruiser"),
]

# Display vehicle information
display_vehicle_info(vehicles)