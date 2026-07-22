# Create Ride class
class Ride:

    # Class variable to count total rides
    total_rides = 0

    # Constructor
    def __init__(self, customer_name):

        # Store customer name
        self.customer_name = customer_name

        # Increase ride counter whenever a new object is created
        Ride.total_rides += 1


# Create ride objects
ride1 = Ride("Ali")
ride2 = Ride("Ahmed")
ride3 = Ride("Hassan")

# Print total rides
print("Total Rides:", Ride.total_rides)