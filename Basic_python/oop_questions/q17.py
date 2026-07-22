# Create Address class
class Address:

    # Constructor
    def __init__(self, city, pincode, state):

        # Private city
        self.__city = city

        # Private pincode
        self.__pincode = pincode

        # Private state
        self.__state = state

    # Getter for city
    def get_city(self):
        return self.__city

    # Getter for pincode
    def get_pincode(self):
        return self.__pincode

    # Getter for state
    def get_state(self):
        return self.__state


# Create Customer class
class Customer:

    # Constructor
    def __init__(self, name, gender, address):

        # Store customer name
        self.name = name

        # Store gender
        self.gender = gender

        # Store Address object
        self.address = address

    # Print shipping label
    def print_shipping_label(self):

        # Print formatted shipping address
        print(
            f"Shipping to: {self.name}, "
            f"{self.address.get_city()}-"
            f"{self.address.get_pincode()}, "
            f"{self.address.get_state()}"
        )


# Create Address object
addr = Address("Lahore", 54000, "Punjab")

# Create Customer object
cust = Customer("Zain", "Male", addr)

# Print shipping label
cust.print_shipping_label()