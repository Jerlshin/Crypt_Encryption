def select_symmetric_algorithm(security_level, performance):
    """
    Select a symmetric encryption algorithm based on security level and performance.
    """
    if security_level == "High" and performance == "Moderate":
        return "AES (Advanced Encryption Standard)"
    elif security_level == "Moderate" and performance == "High":
        return "3DES (Triple Data Encryption Standard)"
    elif security_level == "Low" and performance == "High":
        return "DES (Data Encryption Standard)"
    else:
        return "No suitable symmetric algorithm found."

def select_asymmetric_algorithm(security_level, performance):
    """
    Select an asymmetric encryption or decryption algorithm based on security level and performance.
    """
    if security_level == "High" and performance == "Moderate":
        return "RSA (Rivest-Shamir-Adleman)"
    elif security_level == "Moderate" and performance == "High":
        return "ECC (Elliptic Curve Cryptography)"
    elif security_level == "High" and performance == "Low":
        return "DSA (Digital Signature Algorithm)"
    else:
        return "No suitable asymmetric algorithm found."

def select_hashing_algorithm(security_level, performance):
    """
    Select a hashing algorithm based on security level and performance.
    """
    if security_level == "High" and performance == "Low":
        return "SHA-256 (Secure Hash Algorithm)"
    elif security_level == "Moderate" and performance == "High":
        return "MD5 (Message Digest Algorithm)"
    elif security_level == "Low" and performance == "High":
        return "CRC32 (Cyclic Redundancy Check)"
    else:
        return "No suitable hashing algorithm found."

def decision_support_system(algorithm_type, security_level, performance, data_type):
    """
    Main decision support function to recommend a cryptographic algorithm based on inputs.
    """
    if algorithm_type == "Symmetric" and data_type == "Encryption":
        return select_symmetric_algorithm(security_level, performance)
    elif algorithm_type == "Asymmetric" and data_type in ("Encryption", "Decryption"):
        return select_asymmetric_algorithm(security_level, performance)
    elif algorithm_type == "Hashing" and data_type == "Hashing":
        return select_hashing_algorithm(security_level, performance)
    else:
        return "Invalid input or no suitable algorithm found."

if __name__ == "__main__":
    # Get input from the user
    algorithm_type = input("Enter the algorithm type (Symmetric/Asymmetric/Hashing): ")
    security_level = input("Enter the security level (High/Moderate/Low): ")
    performance = input("Enter the performance requirement (High/Moderate/Low): ")
    data_type = input("Enter the data type (Encryption/Decryption/Hashing): ")

    # Call the decision function and display the result
    decision = decision_support_system(algorithm_type, security_level, performance, data_type)
    print(f"Recommended Cryptographic Algorithm: {decision}")
