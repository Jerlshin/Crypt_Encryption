import socket
import hashlib  # For hashing functionality
# hashlib.sha256(data).hexdigest()

# Function to hash data using SHA-256
def sha256_hash(data):
    """
    Hash the input data using the SHA-256 algorithm.
    Args:
        data (bytes): Data to be hashed.
    Returns:
        str: Hexadecimal representation of the SHA-256 hash.
    """
    return hashlib.sha256(data).hexdigest()

# Function to start the server and listen for incoming connections
def start_server():
    """
    Start a TCP server that listens for incoming client connections.
    The server receives a message, hashes it using SHA-256, and sends the hash back to the client.
    """
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the server to localhost on port 12345
    server_socket.bind(('localhost', 12345)) # start listening to the client
    
    # Allow the server to listen for up to 1 connection at a time
    server_socket.listen(1)
    print("Server is listening on port 12345...")

    # Continuously listen for client connections
    while True:
        # Accept a new connection from a client
        client_socket, addr = server_socket.accept() # accept the new connection socket instance and the address
        print(f"Connection from {addr} has been established.")
        
        # Receive data from the client (maximum 1024 bytes)
        data = client_socket.recv(1024) # recieve the data from the client
        if not data:
            break  # If no data is received, exit the loop

        # Hash the received data using SHA-256
        hashed_data = sha256_hash(data) # encrypt
        
        # Send the hashed data back to the client
        client_socket.send(hashed_data.encode())
        
        # Close the connection to the client
        client_socket.close()

# Call the server function when this script is executed
if __name__ == "__main__":
    start_server()
