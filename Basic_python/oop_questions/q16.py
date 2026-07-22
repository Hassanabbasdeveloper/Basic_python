# Create BankAccount class
class BankAccount:

    # Constructor
    def __init__(self, balance):

        # Private balance variable
        self.__balance = balance

    # Getter method
    def get_balance(self):

        # Return current balance
        return self.__balance

    # Setter method
    def set_balance(self, balance):

        # Check if balance is int or float
        if isinstance(balance, (int, float)):

            # Check if balance is positive
            if balance > 0:

                # Update private balance
                self.__balance = balance

            else:

                # Raise error for negative value
                raise ValueError("Balance must be positive.")

        else:

            # Raise error for invalid data type
            raise TypeError("Balance must be int or float.")


# Create object
account = BankAccount(10000)

# Update balance
account.set_balance(15000)

# Print balance
print(account.get_balance())

# Uncomment to test errors
# account.set_balance(-500)
# account.set_balance("ten thousand")