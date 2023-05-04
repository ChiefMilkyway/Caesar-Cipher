def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    
    return encrypted_text

# Example usage
plaintext = "Hello, World!"
shift = 1
ciphertext = caesar_cipher(plaintext, shift)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
