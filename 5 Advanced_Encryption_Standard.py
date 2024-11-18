# AES S-box
S_BOX = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5,
    0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xFA, 0x59, 0x47, 0xf0,
    0xAD, 0xd4, 0xa2, 0xaf, 0x9c, 0xa8, 0x51, 0xA3,
    0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6,
    0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 0xcd, 0x0c,
    0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7,
    0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73, 0x60, 0x81,
    0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee,
    0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32,
    0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3,
    0xac, 0x62, 0x91, 0x95, 0x0e, 0x98, 0x4c, 0x79,
    0x68, 0x3e, 0x81, 0x69, 0x1f, 0x97, 0x2d, 0x0c
]

# Round constant (Rcon) for AES key expansion
RCON = [
    0x01000000, 0x02000000, 0x04000000, 0x08000000,
    0x10000000, 0x20000000, 0x40000000, 0x80000000,
    0x1b000000, 0x36000000
]

def subword(word):
    """Apply S-box substitution to each byte of a word."""
    # Ensure each byte is valid (0-255 range)
    byte_1 = (word >> 24) & 0xFF
    byte_2 = (word >> 16) & 0xFF
    byte_3 = (word >> 8) & 0xFF
    byte_4 = word & 0xFF
    
    # Apply S-box to each byte
    return ((S_BOX[byte_1] << 24) |
            (S_BOX[byte_2] << 16) |
            (S_BOX[byte_3] << 8) |
            S_BOX[byte_4])

def rotword(word):
    """Perform a cyclic permutation (rotate) on the word."""
    return ((word << 8) & 0xFFFFFFFF) | (word >> 24)

def key_expansion(key):
    """Generate the key schedule for AES-128."""
    # Convert the 16-byte key to a list of 32-bit words
    key_schedule = []
    for i in range(0, 16, 4):
        key_schedule.append(int(key[i:i+2], 16) << 24 |
                            int(key[i+2:i+4], 16) << 16 |
                            int(key[i+4:i+6], 16) << 8 |
                            int(key[i+6:i+8], 16))

    # Generate the key schedule words w[4] to w[43]
    for i in range(4, 44):
        temp = key_schedule[i-1]
        
        # Every 4th word: apply RotWord and SubWord, and XOR with Rcon
        if i % 4 == 0:
            temp = subword(rotword(temp)) ^ RCON[i // 4 - 1]

        # XOR with the word 4 steps earlier in the key schedule
        key_schedule.append(key_schedule[i - 4] ^ temp)

    return key_schedule

def print_key_schedule(key_schedule):
    """Print the key schedule in the required format."""
    for i, word in enumerate(key_schedule):
        print(f"w[{i}] = {word:08x}")

# Input: 16-byte (128-bit) AES key in hexadecimal format
input_key = "2b7e151628aed2a6abf7158809cf4f3c"

# Generate the key schedule
key_schedule = key_expansion(input_key)

# Print the key schedule words w[0] to w[43]
print_key_schedule(key_schedule)
