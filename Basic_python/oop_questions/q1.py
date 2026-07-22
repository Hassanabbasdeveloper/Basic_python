# Create a class named BankAccount
class BankAccount:

    # Constructor to initialize the object
    def __init__(self, balance):

        # Private variable using double underscore
        self.__balance = balance

# Create an object of the class
customer_account = BankAccount(5000)

# Trying to access private variable directly
print(customer_account.__balance)

# This will raise an AttributeError because
# Python performs Name Mangling on private variables.