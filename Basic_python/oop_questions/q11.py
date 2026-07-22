# Create CreditCard class
class CreditCard:

    # Constructor
    def __init__(self, card_number):

        # Private card number
        self.__card_number = card_number

    # Getter method to access private card number
    def get_card_number(self):

        # Return private card number
        return self.__card_number


# Create Customer class
class Customer:

    # Constructor receives CreditCard object
    def __init__(self, name, credit_card):

        # Store customer name
        self.name = name

        # Store CreditCard object (Aggregation)
        self.credit_card = credit_card

    # Display card details
    def show_card(self):

        # Access private data using getter method
        print("Card Number:", self.credit_card.get_card_number())


# Create CreditCard object
card = CreditCard("1234-5678-9012-3456")

# Create Customer object
customer = Customer("Ali", card)

# Display card number
customer.show_card()