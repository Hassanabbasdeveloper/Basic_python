# Create TaxCalculator class
class TaxCalculator:

    # Method with default parameter
    def calculate_tax(self, income, treaty_rate=None):

        # Check if treaty rate is provided
        if treaty_rate is None:

            # Calculate local tax (10%)
            tax = income * 0.10

        else:

            # Calculate international tax
            tax = income * treaty_rate

        # Return tax amount
        return tax


# Create object
calc = TaxCalculator()

# Local tax
print("Local Tax:", calc.calculate_tax(100000))

# International tax
print("International Tax:", calc.calculate_tax(100000, 0.15))