# First Parent class
class WirelessModem:

    # Connect method
    def connect(self):

        # Print modem message
        print("Connected through Wireless Modem")


# Second Parent class
class AudioSpeaker:

    # Connect method
    def connect(self):

        # Print speaker message
        print("Connected through Audio Speaker")


# Child class
class SmartSpeaker(WirelessModem, AudioSpeaker):

    # No extra code
    pass


# Create object
speaker = SmartSpeaker()

# Call connect method
speaker.connect()

# Print MRO
print(SmartSpeaker.__mro__)