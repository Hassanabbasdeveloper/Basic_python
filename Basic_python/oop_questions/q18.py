# Create CloudServer class
class CloudServer:

    # Private class variable
    __active_servers_count = 0

    # Constructor
    def __init__(self):

        # Increase active server count
        CloudServer.__active_servers_count += 1

        # Assign unique server ID
        self.server_id = f"Server-{100 + CloudServer.__active_servers_count}"

    # Static method to get total active servers
    @staticmethod
    def get_active_servers():

        # Return active server count
        return CloudServer.__active_servers_count


# Create objects
server1 = CloudServer()
server2 = CloudServer()
server3 = CloudServer()

# Print IDs
print(server1.server_id)
print(server2.server_id)
print(server3.server_id)

# Print total servers
print("Active Servers:", CloudServer.get_active_servers())