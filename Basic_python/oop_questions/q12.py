# Create Parent class
class Vehicle:

    # Parent constructor
    def __init__(self, brand):

        # Store brand name
        self.brand = brand


# Create Child class
class ElectricCar(Vehicle):

    # Child constructor
    def __init__(self, brand, battery):

        # Call parent constructor
        super().__init__(brand)

        # Store battery capacity
        self.battery = battery

    # Display details
    def display(self):

        # Print brand
        print("Brand:", self.brand)

        # Print battery
        print("Battery:", self.battery)


# Create object
car = ElectricCar("Tesla", "100 kWh")

# Display information
car.display()