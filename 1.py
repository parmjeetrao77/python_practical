# Program 1: Dynamic Command-Line Caesar Cipher Tool

def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char

    return result


def main():
    print("===== Caesar Cipher Tool =====")

    text = input("Enter text: ")
    shift = int(input("Enter shift key: "))

    print("\n1. Encrypt")
    print("2. Decrypt")

    choice = input("Enter your choice: ")

    if choice == "1":
        result = caesar_cipher(text, shift)
        print("Encrypted text:", result)

    elif choice == "2":
        result = caesar_cipher(text, -shift)
        print("Decrypted text:", result)

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
