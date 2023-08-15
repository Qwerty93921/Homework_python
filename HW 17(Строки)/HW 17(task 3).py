def decrypt(text):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = 25
            if char.islower():
                base = ord('a')
                shift = (ord(char) - base - 1) % 26
                decrypted_char = chr(base + shift)
            elif char.isupper():
                base = ord('A')
                shift = (ord(char) - base - 1) % 26
                decrypted_char = chr(base + shift)
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text

def main():
    with open("input3.txt", "r") as input_file:
        encrypted_message = input_file.read().strip()

    decrypted_message = decrypt(encrypted_message)

    with open("output3.txt", "w", encoding="utf-8") as output_file:
        output_file.write(decrypted_message)

if __name__ == "__main__":
    main()

print("Послание дешифровано")
