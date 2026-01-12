# Honey-Encryption

#### Expected output:

```
==============================
  HONEY ENCRYPTION DEMO
==============================

Secret message:
  "Meeting at 10am near library"
Real password: "bluebird42"

=== Honey Encryption ===

Ciphertext (numeric): 48217

Decryption attempts:
[✓] Password 'bluebird42' → Meeting at 10am near library
[?] Password 'password123' → Meeting at 2pm near cafeteria
[?] Password 'admin' → Meeting at 9am near lab
[?] Password 'qwerty' → Meeting at 4pm near office

=== Traditional Encryption ===

Decryption attempts:
[✓] Password 'bluebird42' → Meeting at 10am near library
[✗] Password 'password123' → DECRYPTION FAILED
[✗] Password 'admin' → DECRYPTION FAILED
[✗] Password 'qwerty' → DECRYPTION FAILED

==============================
  BRUTE-FORCE ATTACK SIMULATION
==============================

>>> Attacking Traditional Encryption:

[✗] Tried '123456' → decryption failed
[✗] Tried 'password' → decryption failed
[✗] Tried 'letmein' → decryption failed
[✗] Tried 'admin' → decryption failed
[✗] Tried 'qwerty' → decryption failed
[✓] Tried 'bluebird42' → 'Meeting at 10am near library'
[✗] Tried 'welcome' → decryption failed

Summary:
  Passwords tried: 7
  Successful decryptions: 1
  Failed decryptions: 6

>>> Attacking Honey Encryption:

[✓] Tried '123456' → 'Meeting at 11am near cafeteria'
[✓] Tried 'password' → 'Meeting at 2pm near lab'
[✓] Tried 'letmein' → 'Meeting at 9am near office'
[✓] Tried 'admin' → 'Meeting at 4pm near cafeteria'
[✓] Tried 'qwerty' → 'Meeting at 10am near lab'
[✓] Tried 'bluebird42' → 'Meeting at 10am near library'
[✓] Tried 'welcome' → 'Meeting at 11am near office'

Summary:
  Passwords tried: 7
  Successful decryptions: 7
  Failed decryptions: 0
```