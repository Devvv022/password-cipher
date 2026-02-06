# Simple Password Protection System using Caesar Cipher
# This program demonstrates basic encryption and decryption logic

def encrypt(password, key):
    encrypted_password = ""
    for char in password:
        encrypted_password += chr(ord(char) + key)
    return encrypted_password


def decrypt(encrypted_password, key):
    decrypted_password = ""
    for char in encrypted_password:
        decrypted_password += chr(ord(char) - key)
    return decrypted_password


# Main program
key = 3  # Fixed shift key for cipher

print("=== Password Protection System ===")

password = input("Create your password: ")

encrypted = encrypt(password, key)
print("Encrypted password stored securely:", encrypted)

print("\n--- Login ---")
entered_password = input("Enter your password: ")

decrypted = decrypt(encrypted, key)

if entered_password == decrypted:
    print("Access Granted ✅")
else:
    print("Access Denied ❌")