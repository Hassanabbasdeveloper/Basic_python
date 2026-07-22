# Create DBSession class
class DBSession:

    # Constructor
    def __init__(self, host, port, user):

        # Store immutable credentials tuple
        self.credentials = (host, port, user)


# Create object
session = DBSession("localhost", 3306, "admin")

# Print original tuple
print(session.credentials)

# Try to modify tuple
try:

    # This line raises TypeError
    session.credentials[1] = 8080

# Catch exception
except TypeError as error:

    # Print error message
    print("Error:", error)