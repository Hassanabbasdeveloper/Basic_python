# Create NetworkUtility class
class NetworkUtility:

    # Static method
    @staticmethod
    def is_latency_safe(latency):

        # Check latency
        if latency <= 50:

            # Safe latency
            return True

        else:

            # Unsafe latency
            return False


# Call static method
print(NetworkUtility.is_latency_safe(45))

# Call again
print(NetworkUtility.is_latency_safe(80))