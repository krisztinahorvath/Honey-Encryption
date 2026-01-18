"""
Traditional password-based encryption to compare with Honey Encryption
"""


HEADER = b"HDR:"  # Known prefix to detect wrong passwords


def _xor_bytes(data, key):
    """
    XOR data with a repeating key
    """
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))


def encrypt(message, password):
    """
    Encrypt a message with a password using XOR
    Returns bytes
    """
    if not password:
        raise ValueError("Password cannot be empty")

    plaintext = HEADER + message.encode("utf-8")
    key = password.encode("utf-8")

    return _xor_bytes(plaintext, key)


def decrypt(ciphertext, password):
    """
    Decrypt ciphertext with a password
    Returns plaintext string or None if password is wrong
    """
    if not password:
        raise ValueError("Password cannot be empty")

    key = password.encode("utf-8")
    decrypted = _xor_bytes(ciphertext, key)

    if not decrypted.startswith(HEADER):
        # Wrong password
        return None

    return decrypted[len(HEADER):].decode("utf-8")

