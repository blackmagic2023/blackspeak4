from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_message(message, key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

def main():
    print("Welcome to the Secure Message Encryption and Decryption Tool!")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        message = input("Enter the message you want to encrypt: ")
        key = generate_key()
        cipher_suite = Fernet(key)
        encrypted_message = cipher_suite.encrypt(message.encode())
        combined = encrypted_message + b"||" + key
        print("Encrypted Message with Key:", combined.decode())
    elif choice == "2":
        combined = input("Enter the encrypted message with key: ")
        encrypted_message, key = combined.split("||")
        cipher_suite = Fernet(key.encode())
        decrypted_message = cipher_suite.decrypt(encrypted_message.encode()).decode()
        print("Decrypted Message:", decrypted_message)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
