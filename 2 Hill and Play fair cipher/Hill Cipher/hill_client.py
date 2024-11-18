import socket

# Matrix multiplication (used for encryption and decryption)
def matrix_multiply(A, B):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]

# Modulo operation for matrix elements (used for encryption and decryption)
def mod_matrix(matrix, mod):
    return [[(element % mod + mod) % mod for element in row] for row in matrix]

# Determinant calculation for 3x3 matrix
def determinant_3x3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return (a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g))

# Adjugate of a 3x3 matrix
def adjugate_3x3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return [
        [e * i - f * h, -(b * i - c * h), b * f - c * e],
        [-(d * i - f * g), a * i - c * g, -(a * f - c * d)],
        [d * h - e * g, -(a * h - b * g), a * e - b * d]
    ]

# Matrix inverse mod 26
def matrix_inverse_3x3(matrix, mod):
    det = determinant_3x3(matrix)
    det_mod_inv = mod_inverse(det, mod)
    adj = adjugate_3x3(matrix)
    return mod_matrix([[adj[i][j] * det_mod_inv for j in range(3)] for i in range(3)], mod)

# Modular inverse using Extended Euclidean Algorithm
def mod_inverse(a, mod):
    gcd, x, _ = extended_euclidean_algorithm(a, mod)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return (x % mod + mod) % mod

# Extended Euclidean Algorithm
def extended_euclidean_algorithm(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

# Hill cipher decryption function
def hill_decrypt(cipher_text, key_matrix):
    key_size = len(key_matrix)
    cipher_text = cipher_text.upper()
    cipher_matrix = [ord(char) - ord('A') for char in cipher_text]

    inverse_key_matrix = matrix_inverse_3x3(key_matrix, 26)
    plain_text = ""

    for i in range(0, len(cipher_matrix), key_size):
        block = [[cipher_matrix[i + j] if i + j < len(cipher_matrix) else 0 for j in range(key_size)]]
        plain_block = matrix_multiply(block, inverse_key_matrix)
        plain_block = mod_matrix(plain_block, 26)
        plain_text += ''.join(chr(char + ord('A')) for char in plain_block[0])

    return plain_text.rstrip('X')

KEY_MATRIX = [
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
]

# Client program to connect to server, receive encrypted messages, and decrypt them
def client_program():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(('localhost', 65432))
            print("Connected to server. Waiting for encrypted messages...")
            while True:
                encrypted_message = client_socket.recv(1024).decode().strip()
                if not encrypted_message:
                    break
                print(f"Encrypted message received: {encrypted_message}")
                decrypted_message = hill_decrypt(encrypted_message, KEY_MATRIX)
                print(f"Decrypted message: {decrypted_message}")
    except Exception as e:
        print(f"Client error: {str(e)}")

if __name__ == "__main__":
    client_program()

