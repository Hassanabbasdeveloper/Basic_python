# Create Menu class
class Menu:

    # Constructor
    def __init__(self, food_name):

        # Store food name
        self.food_name = food_name


# Create Restaurant class
class Restaurant:

    # Constructor receives Menu object
    def __init__(self, menu):

        # Store Menu object
        self.menu = menu

    # Display menu
    def show_menu(self):

        # Print food name
        print("Food Item:", self.menu.food_name)


# Create Menu object
menu1 = Menu("Chicken Biryani")

# Pass Menu object into Restaurant object
restaurant = Restaurant(menu1)

# Display menu
restaurant.show_menu()