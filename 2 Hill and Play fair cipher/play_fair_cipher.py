import numpy as np

# Function to convert text to lowercase
def to_lower_case(text):
    return text.lower() # lowercase

# Function to remove spaces from the text
def remove_spaces(text):
    return text.replace(" ", "") # remove the spaces

# Function to generate the Playfair cipher key table
def generate_key_table(key): # key for the encryption
    # Remove spaces, convert to lowercase and replace 'j' with 'i'
    key = remove_spaces(to_lower_case(key))
    key = key.replace('j', 'i')

    # Simply removing the duplicates from the text # 1. create dict (removes the duplicates) # then, again join it as text
    key = ''.join(dict.fromkeys(key)) # {'d': None, 'u': None, 'm': None, 'y': None} # make the keys for the dictionary from the 'key'
    # OUTPUT: dumy

    # Create the alphabet (excluding 'j')
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    key_table = [c for c in key if c in alphabet]

    # Add remaining characters of the alphabet to the key table
    for char in alphabet:
        if char not in key_table:
            key_table.append(char)

    # Convert the key table into a 5x5 matrix
    key_table = np.array(key_table).reshape(5, 5) # 25 alphabest --> excluding the 'j'
    return key_table

# Function to search the positions of two characters in the key table
def search(key_table, a, b):
    # Replace 'j' with 'i' for standardization
    if a == 'j':
        a = 'i'
    if b == 'j':
        b = 'i'

    p1 = p2 = None
    for i in range(5):
        for j in range(5):
            if key_table[i, j] == a:
                p1 = (i, j)
            elif key_table[i, j] == b:
                p2 = (i, j)
    return p1, p2

# Function to handle encryption using Playfair cipher rules
def encrypt(plaintext, key):
    # generate the matrix
    key_table = generate_key_table(key)
    plaintext = remove_spaces(to_lower_case(plaintext)) # process the plain text also

    # Adjust plaintext to even length, adding 'x' if necessary
    if len(plaintext) % 2 != 0:
        plaintext += 'x' # add to the last

    # Encrypt the plaintext
    ciphertext = []
    for i in range(0, len(plaintext), 2): # for the pair of two
        a, b = plaintext[i], plaintext[i + 1] # access two elements -- 1 pair
        p1, p2 = search(key_table, a, b)

        if p1[0] == p2[0]:  # Same row
            ciphertext.append(key_table[p1[0], (p1[1] + 1) % 5])
            ciphertext.append(key_table[p2[0], (p2[1] + 1) % 5])
        elif p1[1] == p2[1]:  # Same column
            ciphertext.append(key_table[(p1[0] + 1) % 5, p1[1]])
            ciphertext.append(key_table[(p2[0] + 1) % 5, p2[1]])
        else:  # Rectangle swap
            ciphertext.append(key_table[p1[0], p2[1]])
            ciphertext.append(key_table[p2[0], p1[1]])

    return ''.join(ciphertext)

# Function to handle decryption using Playfair cipher rules
def decrypt(ciphertext, key):
    key_table = generate_key_table(key)

    # Decrypt the ciphertext
    decrypted_text = []
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        p1, p2 = search(key_table, a, b)

        if p1[0] == p2[0]:  # Same row
            decrypted_text.append(key_table[p1[0], (p1[1] - 1) % 5])
            decrypted_text.append(key_table[p2[0], (p2[1] - 1) % 5])
        elif p1[1] == p2[1]:  # Same column
            decrypted_text.append(key_table[(p1[0] - 1) % 5, p1[1]])
            decrypted_text.append(key_table[(p2[0] - 1) % 5, p2[1]])
        else:  # Rectangle swap
            decrypted_text.append(key_table[p1[0], p2[1]])
            decrypted_text.append(key_table[p2[0], p1[1]])

    return ''.join(decrypted_text)

# Main function to drive the encryption and decryption
if __name__ == "__main__":
    key = "dummy" # this is the key for the encryption
    plaintext = "notebook"  # plan text to be encrypted
    
    # Encrypt the plaintext
    print("Key Text:", key)
    print("Plaintext:", plaintext)
    encrypted_text = encrypt(plaintext, key)
    print("Encrypted Text:", encrypted_text)

    # Decrypt the ciphertext
    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)
