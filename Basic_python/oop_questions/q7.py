# Create Converter class
class Converter:

    # Static method because no object data is required
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):

        # Apply conversion formula
        celsius = (fahrenheit - 32) * 5 / 9

        # Return converted temperature
        return celsius


# Call static method without creating object
result = Converter.fahrenheit_to_celsius(98.6)

# Print result
print("Temperature in Celsius:", result)