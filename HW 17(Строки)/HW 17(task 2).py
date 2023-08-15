def encrypt(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = 1
            if char.islower():
                base = ord('a')
                shift = (ord(char) - base + 1) % 26
                encrypted_char = chr(base + shift)
            elif char.isupper():
                base = ord('A')
                shift = (ord(char) - base + 1) % 26
                encrypted_char = chr(base + shift)
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

def main():
    with open("input2.txt", "r", encoding="utf-8") as input_file:
        message = input_file.read().strip()

    encrypted_message = encrypt(message)

    with open("output2.txt", "w") as output_file:
        output_file.write(encrypted_message)

if __name__ == "__main__":
    main()

print("Послание зашифровано")
