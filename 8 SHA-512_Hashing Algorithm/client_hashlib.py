import socket  # For network communication

# Function to send a message to the server
def send_message(message):
    """
    Connects to the server, sends a message, and prints the hashed response.
    Args:
        message (str): Message to send to the server.
    """
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server at localhost on port 12345
    client_socket.connect(('localhost', 12345)) # connect with the address (localhost, port)
    
    # Send the message to the server
    client_socket.send(message.encode()) # send the message as bytes
    
    # Receive the hashed response from the server (up to 1024 bytes)
    hashed_data = client_socket.recv(1024) # receive upto 1024 bytes
    
    # Print the received hashed data
    print(f"Received hashed data: {hashed_data.decode()}") # decode to value
    
    # Close the connection
    client_socket.close()

# Send an example message to the server
if __name__ == "__main__":
    message = "Hello, Server!"  # Example message to hash
    send_message(message)
