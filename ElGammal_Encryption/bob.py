import socket
from common_elgamal import generate_keys, elgamal_decrypt

# Parameters for ElGamal encryption
p = 467  # Prime number
g = 2    # Primitive root

# Generate Bob's keys
bob_private_key, bob_public_key = generate_keys(p, g)
print(f"Bob's public key: {bob_public_key}")

# Set up Bob's server to receive the encrypted message
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12346))
server_socket.listen(1)
print("Bob's server is listening...")

connection, address = server_socket.accept()
print(f"Connected by {address}")

# Receive and decrypt the message
data = connection.recv(1024).decode().split(',')
c1 = int(data[0])
c2 = int(data[1])
decrypted_message = elgamal_decrypt(p, bob_private_key, c1, c2)
print(f"Decrypted message: {decrypted_message}")

connection.close()
server_socket.close()

