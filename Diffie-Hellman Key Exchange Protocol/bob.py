import socket
import random

# Function to perform modular exponentiation
def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

# Diffie-Hellman key exchange function
def diffie_hellman_exchange(p, g, private_key):
    public_value = mod_exp(g, private_key, p)
    return public_value

# Generate a shared secret
def generate_shared_secret(received_public_value, private_key, p):
    shared_secret = mod_exp(received_public_value, private_key, p)
    return shared_secret

# Set up common parameters p (prime) and g (primitive root)
p = 23
g = 5

# Bob's private key (random)
bob_private_key = random.randint(1, p - 1)

# Bob's socket to communicate with Alice
bob_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bob_socket.bind(('localhost', 12346))
bob_socket.listen(1)

connection, address = bob_socket.accept()

# Receive Alice's public value
alice_public_value = int(connection.recv(1024).decode())

# Bob's public value
bob_public_value = diffie_hellman_exchange(p, g, bob_private_key)
connection.send(str(bob_public_value).encode())  # Send public value to Alice

# Compute the shared secret
bob_shared_secret = generate_shared_secret(alice_public_value, bob_private_key, p)
print(f"Bob's Shared Secret: {bob_shared_secret}")

connection.close()

