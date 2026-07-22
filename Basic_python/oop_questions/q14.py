# Create ShoppingCart class
class ShoppingCart:

    # Constructor
    def __init__(self, total_bill):

        # Store total bill
        self.total_bill = total_bill

    # Overload + operator
    def __add__(self, other):

        # Return sum of both bills
        return self.total_bill + other.total_bill


# Create objects
cart1 = ShoppingCart(1500)

cart2 = ShoppingCart(2500)

# Use + operator
total = cart1 + cart2

# Print total bill
print("Total Bill:", total)