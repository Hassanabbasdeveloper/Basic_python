# Create WeatherStation class
class WeatherStation:

    # Constructor
    def __init__(self, temperature):

        # Private temperature
        self.__temperature = temperature

    # Getter method
    def get_temperature(self):

        # Return temperature
        return self.__temperature


# Create object
weather = WeatherStation(32)

# Display temperature
print(weather.get_temperature())