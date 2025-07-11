def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around alphabet
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  

    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  

def main():
    print("=== Caesar Cipher Tool ===")
    while True:
        choice = input("Choose an option (encrypt / decrypt / exit): ").strip().lower()

        if choice == "encrypt":
            message = input("Enter message to encrypt: ")
            shift = int(input("Enter shift value (e.g., 3): "))
            encrypted = caesar_encrypt(message, shift)
            print("Encrypted message:", encrypted)

        elif choice == "decrypt":
            message = input("Enter message to decrypt: ")
            shift = int(input("Enter shift value (e.g., 3): "))
            decrypted = caesar_decrypt(message, shift)
            print("Decrypted message:", decrypted)

        elif choice == "exit":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please type 'encrypt', 'decrypt', or 'exit'.")

if __name__ == "__main__":
    main()
