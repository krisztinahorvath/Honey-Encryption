"""
Implements the core Honey Encryption logic
"""


import hashlib
from dte import encode, decode, TOTAL_RANGE


def _password_to_value(password, total_range):
    """
    Deterministically map a password string to a numeric value
    """
    # Hash password deterministically
    h = hashlib.sha256(password.encode()).digest()

    # Convert hash to integer
    value = int.from_bytes(h, byteorder="big")

    # Reduce into DTE range
    return value % total_range

def honey_encrypt(message, password):
    """
    Encrypt a message using Honey Encryption
    Returns a numeric ciphertext
    """
    # Get numeric range for message
    low, high = encode(message)

    # Use midpoint of message range for stability
    message_value = (low + high) // 2

    # Derive password-based offset
    pw_value = _password_to_value(password, TOTAL_RANGE)

    # Combine message and password
    ciphertext = (message_value + pw_value) % TOTAL_RANGE

    return ciphertext

def honey_decrypt(ciphertext, password):
    """
    Decrypt a ciphertext using Honey Encryption
    Always returns a valid plaintext message
    """
     # Derive password-based offset
    pw_value = _password_to_value(password, TOTAL_RANGE)

    # Reverse combination
    decoded_value = (ciphertext - pw_value) % TOTAL_RANGE

    # Decode into a valid message
    return decode(decoded_value)