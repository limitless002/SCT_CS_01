def caesar_cipher_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    if choice == 'e':
        result = caesar_cipher_encrypt(message, shift)
        print("Encrypted message:", result)
    elif choice == 'd':
        result = caesar_cipher_decrypt(message, shift)
        print("Decrypted message:", result)
    else:
        print("Invalid choice. Please type 'e' or 'd'.")

if __name__ == "__main__":
    main()
