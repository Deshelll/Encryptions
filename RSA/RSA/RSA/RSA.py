import random
from sympy import isprime


def generate_prime_candidate(length):
    """Generate an odd integer randomly"""
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1 # Устанавливаю старший и младший биты в 1 (гарантия нечетности)
    return p

def generate_prime_number(length=1024):
    """Generate a prime number of specified length"""
    p = 4
    while not isprime(p):  # Проверка на простоту числа
        p = generate_prime_candidate(length)
    return p

def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b != 0:
        a, b = b, a % b  # алгоритм Евклида
    return a

def multiplicative_inverse(e, phi):
    """Find the multiplicative inverse of e modulo phi"""
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2, x1, d, y1 = x1, x, y1, y
    if temp_phi == 1:
        return d + phi

def generate_keypair(p, q):
    """Generate a key pair of public and private keys"""
    n = p * q  # Модуль RSA
    phi = (p-1) * (q-1)  # Функция Эйлера
    e = random.randrange(1, phi)  # Выбираю открытый экспонент
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)  # Гарантирую, что e и phi взаимно простые
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)  # Генерация закрытого ключа

    return ((e, n), (d, n))  # Публичный и приватный ключи

def encrypt(pk, plaintext):
    """Encrypt the plaintext using the public key"""
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]  # Шифрование каждого символа
    return cipher

def decrypt(pk, ciphertext):
    """Decrypt the ciphertext using the private key"""
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)




if __name__ == '__main__':
    print("Generating large prime numbers. This may take a few moments...")
    p = generate_prime_number(1024)
    q = generate_prime_number(1024)
    public, private = generate_keypair(p, q)
    print("Your public key is ", public)
    print("Your private key is ", private)
    message = input("Enter a message to encrypt: ")
    encrypted_msg = encrypt(public, message)
    print("Encrypted message: ", ''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with private key ", private)
    print("Your message is:")
    print(decrypt(private, encrypted_msg))
