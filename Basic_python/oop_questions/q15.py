# Create TaxCalculator class
class TaxCalculator:

    # Method with default argument
    def calculate_tax(self, income, tax_rate=None):

        # Check if tax_rate is provided
        if tax_rate is None:

            # Calculate local tax (10%)
            tax = income * 0.10

        else:

            # Calculate international tax
            tax = income * tax_rate

        # Return tax amount
        return tax


# Create object
calculator = TaxCalculator()

# Local income tax
print("Local Tax:", calculator.calculate_tax(50000))

# International income tax
print("International Tax:", calculator.calculate_tax(50000, 0.18))