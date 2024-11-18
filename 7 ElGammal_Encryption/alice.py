import socket
from common_elgamal import elgamal_encrypt

# Parameters for ElGamal encryption
p = 467  # Prime number
g = 2    # Primitive root

# Get Bob's public key and message from the user
bob_public_key = int(input("Enter Bob's public key: "))
message = int(input("Enter the message to send to Bob (as a number): "))

# Encrypt the message using Bob's public key
c1, c2 = elgamal_encrypt(p, g, bob_public_key, message)
print(f"Encrypted message: c1={c1}, c2={c2}")

# Send the encrypted message to the attacker
attacker_address = ('localhost', 12347)  # Attacker's port
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(attacker_address)
client_socket.send(f"{c1}, {c2}".encode())
client_socket.close()

