# Create CartItem class
class CartItem:

    # Constructor
    def __init__(self, item_name, quantity, price):

        # Store item name
        self.item_name = item_name

        # Store quantity
        self.quantity = quantity

        # Store price
        self.price = price


# Create multiple CartItem objects
item1 = CartItem("Laptop", 1, 80000)
item2 = CartItem("Mouse", 2, 1500)
item3 = CartItem("Keyboard", 1, 3500)

# Store objects in a list
cart = [item1, item2, item3]

# Variable to store total cost
total_cost = 0

# Loop through cart items
for item in cart:

    # Calculate item total
    total_cost += item.quantity * item.price

# Print total cart value
print("Total Cart Value:", total_cost)