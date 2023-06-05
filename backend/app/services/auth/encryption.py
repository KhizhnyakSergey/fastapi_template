import base64


from cryptography.fernet import Fernet


def get_encrypted_key(key: str) -> str:
    
    random_cipher_key = Fernet.generate_key()
    cipher = Fernet(random_cipher_key)
    encrypted_key = base64.b64encode(cipher.encrypt(key.encode('utf-8'))).decode('utf-8')

    return f'{random_cipher_key.decode()}:{encrypted_key}'


def get_decrypted_value(encrypted_value: str, cipher_key: Fernet) -> str:
    
    cipher = Fernet(cipher_key)
    return cipher.decrypt(base64.b64decode(encrypted_value)).decode('utf-8')


