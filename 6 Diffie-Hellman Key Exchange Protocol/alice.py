import socket # socket programming
import random

# Function to perform modular exponentiation
def mod_exp(base, exp, mod):
    return pow(base, exp, mod) # base ^ exp modulus (mod)

# Diffie-Hellman key exchange function
def diffie_hellman_exchange(p, g, private_key):
    public_value = mod_exp(g, private_key, p)
    return public_value

# Generate a shared secret
def generate_shared_secret(received_public_value, private_key, p):
    shared_secret = mod_exp(received_public_value, private_key, p) # k1 = 
    return shared_secret

# Set up common parameters p (prime) and g (primitive root)
p = 23 # prime number
g = 5 # primitive root of the prime number p

# Alice's private key (random)
alice_private_key = random.randint(1, p - 1) # including both the boundaries 

# Alice's socket to communicate with Bob
alice_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
alice_socket.connect(('localhost', 12346)) # connect to the port

# Alice's public value
alice_public_value = diffie_hellman_exchange(p, g, alice_private_key) # send the prime number, primitive root, X_a
alice_socket.send(str(alice_public_value).encode())  # Send public value to Bob  # convert to bytes b'values'

# Receive Bob's public value
bob_public_value = int(alice_socket.recv(1024).decode())

# Compute the shared secret
alice_shared_secret = generate_shared_secret(bob_public_value, alice_private_key, p)
print(f"Alice's Shared Secret: {alice_shared_secret}")

alice_socket.close()

