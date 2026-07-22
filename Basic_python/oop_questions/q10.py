# Create Parent class
class Watch:

    # Parent method
    def show_time(self):

        # Print current time
        print("Current Time: 10:30 AM")


# Child class inherits Watch
class SmartWatch(Watch):

    # No extra code
    pass


# Create child object
smart_watch = SmartWatch()

# Call parent method using child object
smart_watch.show_time()