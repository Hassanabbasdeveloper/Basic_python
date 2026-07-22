# Create DoorLock class
class DoorLock:

    # Constructor
    def __init__(self, pin):
        # Private PIN
        self.__pin = pin

    # Setter method
    def set_pin(self, new_pin):

        # Check if PIN contains only digits
        if new_pin.isdigit():

            # Update private PIN
            self.__pin = new_pin

            # Success message
            print("PIN updated successfully.")

        else:

            # Error message
            print("Error: PIN should contain digits only.")

    # Getter method
    def get_pin(self):

        # Return private PIN
        return self.__pin


# Create object
lock = DoorLock("1234")

# Valid PIN
lock.set_pin("5678")

# Invalid PIN
lock.set_pin("12AB")

# Print current PIN
print(lock.get_pin())