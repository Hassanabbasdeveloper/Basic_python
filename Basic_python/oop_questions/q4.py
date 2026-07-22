class Bank:

    def __init__(self):
        self.__balance = 5000


account = Bank()

# Access using name mangling
print(account._Bank__balance)