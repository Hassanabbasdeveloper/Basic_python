# Create SmartLock class
class SmartLock:

    # Constructor
    def __init__(self, pin):

        # Private PIN
        self.__pin = pin

    # Setter method
    def set_pin(self, new_pin):

        # Check length and digits
        if len(new_pin) == 4 and new_pin.isdigit():

            # Update PIN
            self.__pin = new_pin

            # Success message
            print("PIN Updated Successfully.")

        else:

            # Validation error
            print("Invalid PIN. PIN must contain exactly 4 digits.")

    # Unlock method
    def unlock(self, input_pin):

        # Compare entered PIN with stored PIN
        if input_pin == self.__pin:

            # Unlock success
            print("Unlocked")

        else:

            # Wrong PIN
            print("Access Denied")


# Create object
lock = SmartLock("1234")

# Update PIN
lock.set_pin("9081")

# Unlock
lock.unlock("9081")