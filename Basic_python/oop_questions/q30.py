# Create UserProfile class
class UserProfile:

    # Constructor
    def __init__(self, name):

        # Store user name
        self.name = name


# Create first object
user1 = UserProfile("Zain")

# Create alias reference
user2 = user1

# Update alias object
user2.name = "Ahmad"

# Print both names
print("User1:", user1.name)
print("User2:", user2.name)

# Print memory addresses
print("User1 ID:", id(user1))
print("User2 ID:", id(user2))