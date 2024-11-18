# Function to compute the GCD of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to compute the modular inverse using the Extended Euclidean Algorithm
def inverse(a, b):
    t1, t2 = 0, 1
    original_a = a
    while b != 0:
        q = a // b
        r = a % b
        a, b = b, r
        t = t1 - q * t2
        t1, t2 = t2, t
    if a != 1:
        print("Inverse does not exist.")
        return -1  # Return -1 if inverse does not exist
    if t1 < 0:
        t1 += original_a
    return t1

# Function to check if all moduli are pairwise coprime
def are_coprime(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if gcd(arr[i][1], arr[j][1]) != 1:  # Check if moduli are coprime
                print(f"Moduli {arr[i][1]} and {arr[j][1]} are not coprime!")
                return False
    return True

# Function to solve the system of congruences using the Chinese Remainder Theorem
def chinese_remainder_theorem(n, arr):
    M = 1
    # Step 1: Multiply all moduli (m1, m2, ..., mn)
    for i in range(n):
        M *= arr[i][1]  # arr[i][1] is the modulus mi
    
    ARR = [0] * n  # This will hold M_i values (product of all moduli except mi)
    inv = [0] * n  # This will hold the modular inverses of M_i modulo mi
    
    # Step 2: Calculate M_i for each modulus
    for i in range(n):
        ARR[i] = M // arr[i][1]  # M_i calculation
    
    # Step 3: Calculate the modular inverse of each M_i modulo mi
    for i in range(n):
        inv[i] = inverse(arr[i][1], ARR[i])  # Modular inverse calculation
    
    # Step 4: Apply the CRT formula to compute X
    X = 0
    for i in range(n):
        X += arr[i][0] * ARR[i] * inv[i]  # Apply the formula X = Σ ai * M_i * inv(M_i)
    
    X = X % M  # Final value of X, modulo M
    return X

# Main function to take user input and solve the system of congruences
if __name__ == "__main__":
    
    # Step 1: Get the number of equations
    n = int(input("Enter the number of equations: "))
    arr = []
    
    print("Enter the a and b values of each equation (a mod b): ")
    # Step 2: Read the equations
    for i in range(n):
        a, b = map(int, input().split())  # Read each pair of (a, b)
        arr.append([a, b])
    
    # Step 3: Check if moduli are pairwise coprime
    if not are_coprime(arr):
        print("Cannot solve: Moduli are not pairwise coprime.")
    else:
        # Step 4: Solve the system using the Chinese Remainder Theorem
        result = chinese_remainder_theorem(n, arr)
        print(f"The value of X is: {result}")
