from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding



from os import urandom

def encrypt_data(data, key):
    # Генерация случайного инициализационного вектора
    iv = urandom(16)
    
    # Создание объекта шифра
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    
    # Шифрование данных
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    return iv, encrypted_data

def decrypt_data(iv, encrypted_data, key):
    # Создание объекта шифра
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    
    # Дешифрование данных
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
    
    return unpadded_data





key = urandom(16) 
data = b"Slim Shake" 

iv, encrypted = encrypt_data(data, key)
print("Encrypted:", encrypted)

decrypted = decrypt_data(iv, encrypted, key)
print("Decrypted:", decrypted)
