
def generate_shifts(keyword):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifts = []
    for letter in keyword:
        shifts.append(alphabet.index(letter.lower()))
    return shifts

def caesar_cipher_encrypt(text, keyword):
    shifts = generate_shifts(keyword)
    encrypted_text = ''
    alphabet = 'catworldsun'
    for i, letter in enumerate(text.lower()):
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shifts[i % len(shifts)]) % len(alphabet)
            encrypted_text += alphabet[shifted_position]
        else:
            encrypted_text += letter
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, keyword):
    shifts = generate_shifts(keyword)
    decrypted_text = ''
    alphabet = 'catworldsun'
    for i, letter in enumerate(encrypted_text.lower()):
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) - shifts[i % len(shifts)]) % len(alphabet)
            decrypted_text += alphabet[shifted_position]
        else:
            decrypted_text += letter
    return decrypted_text

keyword = "key"
text = "My name is Andrey"
encrypted = caesar_cipher_encrypt(text, keyword)
decrypted = caesar_cipher_decrypt(encrypted, keyword)

print(f"Original: {text}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
