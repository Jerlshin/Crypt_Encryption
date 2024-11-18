import socket
import numpy as np

def matrix_multiply(A, B):
    return np.dot(A, B)

def mod_matrix(matrix, mod):
    return np.mod(matrix, mod)

def hill_encrypt(plain_text, key_matrix):
    key_size = len(key_matrix)
    plain_text = plain_text.replace(" ", "").upper()
    padded_length = ((len(plain_text) + key_size - 1) // key_size) * key_size
    padded_text = plain_text.ljust(padded_length, 'X')

    plain_matrix = np.array([ord(char) - ord('A') for char in padded_text])
    cipher_text = ""

    for i in range(0, len(plain_matrix), key_size):
        block = plain_matrix[i:i+key_size].reshape(1, -1)
        cipher_block = np.dot(block, key_matrix)
        cipher_block = np.mod(cipher_block, 26)
        cipher_text += ''.join([chr(int(x) + ord('A')) for x in cipher_block.flatten()])

    return cipher_text

def server_program(key_matrix):
    host = '127.0.0.1'
    port = 65432

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server is waiting for connections...")

    conn, address = server_socket.accept()
    print(f"Connection established with {address}")

    while True:
        message = input("Enter the message to encrypt (or 'exit' to quit): ").strip()
        
        if message.lower() == 'exit':
            print("Server shutting down.")
            break

        encrypted_message = hill_encrypt(message, key_matrix)
        conn.send(encrypted_message.encode())
        print(f"Encrypted message sent: {encrypted_message}")

    conn.close()

if __name__ == "__main__":
    key_matrix = np.array([
        [6, 24, 1],
        [13, 16, 10],
        [20, 17, 15]
    ])
    server_program(key_matrix)

