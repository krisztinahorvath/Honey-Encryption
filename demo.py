from honey_encrypt import honey_encrypt, honey_decrypt
from baseline import encrypt as base_encrypt, decrypt as base_decrypt
from attack_sim import run_attack

"""
Demonstration of Honey Encryption vs traditional encryption

Structure:
- Encrypt a chosen message with a chosen password
- Decrypt it with both correct and incorrect passwords
- Run the attack simulation and display results

"""
# -----------------------------
# Demo params
# -----------------------------
SECRET_MESSAGE = "Meeting at 10am near library"
REAL_PASSWORD = "bluebird42"

WRONG_PASSWORDS = [
    "password123",
    "admin",
    "qwerty",
]

ATTACK_PASSWORDS = [
    "123456",
    "password",
    "letmein",
    "admin",
    "qwerty",
    "bluebird42",   # correct one (unknown to attacker)
    "welcome",
]

def main():
    print("\n==============================")
    print("  HONEY ENCRYPTION DEMO")
    print("==============================\n")

    print("Secret message:")
    print(f'  "{SECRET_MESSAGE}"')
    print(f'Real password: "{REAL_PASSWORD}"\n')

    # --------------------------------------------------
    # Honey Encryption demo
    # --------------------------------------------------
    print("=== Honey Encryption ===\n")

    honey_ciphertext = honey_encrypt(SECRET_MESSAGE, REAL_PASSWORD)
    print(f"Ciphertext (numeric): {honey_ciphertext}\n")

    print("Decryption attempts:")
    print(f"[✓] Password '{REAL_PASSWORD}' → "
          f"{honey_decrypt(honey_ciphertext, REAL_PASSWORD)}")

    for pw in WRONG_PASSWORDS:
        print(f"[?] Password '{pw}' → "
              f"{honey_decrypt(honey_ciphertext, pw)}")

    # --------------------------------------------------
    # Traditional encryption demo
    # --------------------------------------------------
    print("\n=== Traditional Encryption ===\n")

    base_ciphertext = base_encrypt(SECRET_MESSAGE, REAL_PASSWORD)

    print("Decryption attempts:")
    print(f"[✓] Password '{REAL_PASSWORD}' → "
          f"{base_decrypt(base_ciphertext, REAL_PASSWORD)}")

    for pw in WRONG_PASSWORDS:
        result = base_decrypt(base_ciphertext, pw)
        print(f"[✗] Password '{pw}' → {result}")

    # --------------------------------------------------
    # Brute-force attack simulation
    # --------------------------------------------------
    print("\n==============================")
    print("  BRUTE-FORCE ATTACK SIMULATION")
    print("==============================")

    run_attack(
        encrypt_func=base_encrypt,
        decrypt_func=base_decrypt,
        message=SECRET_MESSAGE,
        real_password=REAL_PASSWORD,
        password_list=ATTACK_PASSWORDS,
        label="Traditional Encryption"
    )

    run_attack(
        encrypt_func=honey_encrypt,
        decrypt_func=honey_decrypt,
        message=SECRET_MESSAGE,
        real_password=REAL_PASSWORD,
        password_list=ATTACK_PASSWORDS,
        label="Honey Encryption"
    )

if __name__ == "__main__":
    main()
