"""
Simulates a brute-force password attack.
"""


def run_attack(encrypt_func, decrypt_func, message,
               real_password, password_list, label):
    ciphertext = encrypt_func(message, real_password)

    successes = 0
    failures = 0

    for pw in password_list:
        result = decrypt_func(ciphertext, pw)

        if result is None or result == "DECRYPTION FAILED":
            failures += 1
            print(f"[✗] Tried '{pw}' → decryption failed")
        else:
            successes += 1
            print(f"[✓] Tried '{pw}' → '{result}'")

    print("\nSummary:")
    print(f"  Passwords tried: {len(password_list)}")
    print(f"  Successful decryptions: {successes}")
    print(f"  Failed decryptions: {failures}")
