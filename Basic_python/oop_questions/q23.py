# Create Parent class
class PaymentGateway:

    # Parent method
    def process_payment(self, amount):

        # Default payment message
        print(f"Processing Rs.{amount}")


# JazzCash class
class JazzCash(PaymentGateway):

    # Override method
    def process_payment(self, amount):

        # Calculate fee
        fee = amount * 0.02

        # Print payment details
        print(f"Processing transaction of Rs.{amount} via JazzCash with Rs.{fee} fee")


# EasyPaisa class
class EasyPaisa(PaymentGateway):

    # Override method
    def process_payment(self, amount):

        # Calculate fee
        fee = amount * 0.015

        # Print payment details
        print(f"Processing transaction of Rs.{amount} via EasyPaisa with Rs.{fee} fee")


# NayaPay class
class NayaPay(PaymentGateway):

    # Override method
    def process_payment(self, amount):

        # Calculate fee
        fee = amount * 0.01

        # Print payment details
        print(f"Processing transaction of Rs.{amount} via NayaPay with Rs.{fee} fee")


# Create objects
gateway1 = JazzCash()
gateway2 = EasyPaisa()
gateway3 = NayaPay()

# Call methods
gateway1.process_payment(10000)
gateway2.process_payment(10000)
gateway3.process_payment(10000)