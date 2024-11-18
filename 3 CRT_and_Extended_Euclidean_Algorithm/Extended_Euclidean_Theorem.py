# Function to compute the GCD of two numbers using the Euclidean Algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Extended Euclidean Algorithm to find the GCD of a and b, and the coefficients x and y such that:
# a * x + b * y = gcd(a, b)
def extended_euclidean_algorithm(a, b):
    # x0, x1 are coefficients for a
    # y0, y1 are coefficients for b
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q = a // b  # Quotient
        r = a % b   # Remainder

        # Update the values of a, b
        a, b = b, r

        # Update the coefficients
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    # Return the GCD and the coefficients (x, y) for the equation a * x + b * y = gcd(a, b)
    return a, x0, y0

# Function to find the modular inverse of a modulo m using the Extended Euclidean Algorithm
def mod_inverse(a, m):
    gcd, x, y = extended_euclidean_algorithm(a, m)
    if gcd != 1:
        print("Modular inverse does not exist.")
        return None
    else:
        # The modular inverse is x % m, but it needs to be positive
        return x % m

# Testing the Extended Euclidean Algorithm
if __name__ == "__main__":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    # Find the GCD and the coefficients x, y such that a * x + b * y = gcd(a, b)
    gcd_value, x, y = extended_euclidean_algorithm(a, b)
    print(f"GCD({a}, {b}) = {gcd_value}")
    print(f"Coefficients: x = {x}, y = {y}")
    
    # Example for Modular Inverse
    m = int(input("Enter m to find modular inverse of a modulo m: "))
    inverse = mod_inverse(a, m)
    if inverse is not None:
        print(f"The modular inverse of {a} modulo {m} is: {inverse}")
