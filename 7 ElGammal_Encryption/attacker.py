import socket

# Ports
attacker_port = 12347  # Attacker listens on this port
bob_port = 12346       # Bob's port to forward messages to

# Create socket for the attacker
attacker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
attacker_socket.bind(('localhost', attacker_port))
attacker_socket.listen(1)
print(f"Attacker listening on port {attacker_port}...")

# Accept connection from Alice
conn, addr = attacker_socket.accept()
print(f"Connected by {addr}")

# Receive the encrypted message
data = conn.recv(1024).decode().split(',')
c1 = int(data[0])
c2 = int(data[1])
print(f"Intercepted encrypted message: c1={c1}, c2={c2}")

# Forward the message to Bob
bob_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bob_socket.connect(('localhost', bob_port))
bob_socket.send(f"{c1}, {c2}".encode())
bob_socket.close()
conn.close()
attacker_socket.close()

