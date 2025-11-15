 SCT_CS_01
A simple Python implementation of the Caesar Cipher encryption and decryption algorithm. 
Caesar Cipher CLI Tool

A beginner-friendly Python program that implements the classic Caesar Cipher encryption and decryption technique. This command-line tool allows users to encrypt or decrypt messages using a shift-based substitution cipher.

 What is the Caesar Cipher?

The Caesar Cipher is one of the oldest known encryption techniques. It works by shifting each letter in a message by a fixed number of positions in the alphabet. For example, with a shift of 3, `A` becomes `D`, `B` becomes `E`, and so on.

 Features

- Encrypt any text message using a custom shift value
- Decrypt messages encrypted with the Caesar Cipher
- Preserves letter casing (uppercase/lowercase)
- Ignores and retains non-alphabetic characters (e.g., punctuation, numbers)

 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/limitless002/caesar-cipher-cli.git
   cd caesar-cipher-cli
   - Run the script:
python caesar_cipher.py
- Follow the prompts:
- Choose to encrypt (e) or decrypt (d)
- Enter your message
- Enter a shift value (integer)
- 
Example Caesar Cipher Program
Type 'e' to encrypt or 'd' to decrypt: e
Enter your message: Hello, World!
Enter the shift value (integer): 3
Encrypted message: Khoor, Zruog!
 How It Works- Encryption: Shifts each alphabetic character forward by the specified number of positions.
- Decryption: Reverses the shift to retrieve the original message.
