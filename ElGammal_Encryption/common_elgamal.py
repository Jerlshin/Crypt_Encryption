import random

# Modular Exponentiation: (base^exp) % mod
def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

# Key generation for ElGamal
def generate_keys(p, g):
    private_key = random.randint(1, p-2)
    public_key = mod_exp(g, private_key, p)
    return private_key, public_key

# ElGamal encryption
def elgamal_encrypt(p, g, public_key, message):
    k = random.randint(1, p-2)  # Random number
    c1 = mod_exp(g, k, p)
    c2 = (message * mod_exp(public_key, k, p)) % p
    return c1, c2

# ElGamal decryption
def elgamal_decrypt(p, private_key, c1, c2):
    s = mod_exp(c1, private_key, p)  # Shared secret
    s_inv = mod_exp(s, p-2, p)  # Modular inverse of s
    message = (c2 * s_inv) % p
    return message

