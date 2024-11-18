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

# Mallory's private keys
mallory_private_key_alice = random.randint(1, p - 1)
mallory_private_key_bob = random.randint(1, p - 1)

# Mallory's socket to intercept communication between Alice and Bob
mallory_socket_alice = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mallory_socket_bob = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mallory_socket_alice.bind(('localhost', 12345))
mallory_socket_alice.listen(1)
connection_alice, address_alice = mallory_socket_alice.accept()

# Intercept Alice's public value
alice_public_value = int(connection_alice.recv(1024).decode())
print(f"Mallory intercepted Alice's public value: {alice_public_value}")

# Compute Mallory's public value for Alice
mallory_public_value_alice = diffie_hellman_exchange(p, g, mallory_private_key_alice)
connection_alice.send(str(mallory_public_value_alice).encode())  # Send Mallory's value to Alice

# Compute shared secret with Alice
mallory_shared_secret_alice = generate_shared_secret(alice_public_value, mallory_private_key_alice, p)
print(f"Mallory's Shared Secret with Alice: {mallory_shared_secret_alice}")

# Now intercept Bob's side
mallory_socket_bob.connect(('localhost', 12346))

# Send Mallory's public value to Bob (pretending to be Alice)
mallory_public_value_bob = diffie_hellman_exchange(p, g, mallory_private_key_bob)
mallory_socket_bob.send(str(mallory_public_value_bob).encode())  # Send Mallory's value to Bob

# Receive Bob's public value
bob_public_value = int(mallory_socket_bob.recv(1024).decode())
print(f"Mallory intercepted Bob's public value: {bob_public_value}")

# Compute shared secret with Bob
mallory_shared_secret_bob = generate_shared_secret(bob_public_value, mallory_private_key_bob, p)
print(f"Mallory's Shared Secret with Bob: {mallory_shared_secret_bob}")

mallory_socket_bob.close()
connection_alice.close()
mallory_socket_alice.close()

