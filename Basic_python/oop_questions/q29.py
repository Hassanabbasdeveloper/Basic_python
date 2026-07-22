# Create Parent class
class Validator:

    # Parent method
    def validate(self):

        # Print validation message
        print("Parent Validation Successful")


# Create Child class
class StrictValidator(Validator):

    # Override method
    def validate(self):

        try:

            # Wrong recursive call
            self.validate()

        except RecursionError:

            # Handle recursion error
            print("RecursionError: Infinite recursion detected.")


# Create object
strict_val = StrictValidator()

# Call method
strict_val.validate()