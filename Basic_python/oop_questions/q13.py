# Create Parent class
class Media:

    # Parent method
    def play(self):

        # Print parent message
        print("Playing media...")


# Create Child class
class Mp3Player(Media):

    # Override parent method
    def play(self):

        # Print child message
        print("Playing MP3 music...")


# Create child object
player = Mp3Player()

# Call play method
player.play()