# Create Parent class
class Vehicle:

    # Parent constructor
    def __init__(self, price, brand, engine_no):

        # Store price
        self.price = price

        # Store brand
        self.brand = brand

        # Store engine number
        self.engine_no = engine_no


# Create Child class
class ElectricCar(Vehicle):

    # Child constructor
    def __init__(self, price, brand, engine_no, battery_capacity, charging_time):

        # Call parent constructor
        super().__init__(price, brand, engine_no)

        # Store battery capacity
        self.battery_capacity = battery_capacity

        # Store charging time
        self.charging_time = charging_time

    # Display details
    def display(self):

        # Print vehicle details
        print("Price:", self.price)
        print("Brand:", self.brand)
        print("Engine No:", self.engine_no)
        print("Battery:", self.battery_capacity)
        print("Charging Time:", self.charging_time)


# Create object
car = ElectricCar(25000, "Tesla", "EV909", "100kWh", "4 Hours")

# Display details
car.display()