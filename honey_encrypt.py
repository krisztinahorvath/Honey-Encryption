"""
Implements the core Honey Encryption logic

This file should:
- Derive a deterministic numeric value from a password
- Use the DTE to encrypt a message into a numeric ciphertext
- Decrypt any ciphertext + password into a valid plaintext message

Correct passwords should decrypt to the original message
Incorrect passwords should decrypt to a different but plausible message

This demonstrates the core idea of Honey Encryption
"""


# TODO:
# [ ] Implement password-to-seed derivation
# [ ] Map seed into DTE numeric range
# [ ] Implement honey_encrypt()
# [ ] Implement honey_decrypt()
# [ ] Ensure wrong passwords yield plausible plaintexts

def _password_to_value(password, total_range):
    """
    Deterministically map a password string to a numeric value.
    """
    raise NotImplementedError

def honey_encrypt(message, password):
    """
    Encrypt a message using Honey Encryption.
    Returns a numeric ciphertext.
    """
    raise NotImplementedError

def honey_decrypt(ciphertext, password):
    """
    Decrypt a ciphertext using Honey Encryption.
    Always returns a valid plaintext message.
    """
    raise NotImplementedError
