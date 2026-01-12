"""
Implements a simplified Distribution-Transforming Encoder (DTE).

This file should:
- Map each valid message to a unique numeric range.
- Define a TOTAL_RANGE covering all messages.
- Provide deterministic encode() and decode() functions:
    - encode(message) -> (low, high)
    - decode(value) -> message

The goal is that *any* numeric value in TOTAL_RANGE decodes
to a valid, plausible message.
This is an educational DTE, not a cryptographically secure one.
"""


# TODO:
# [ ] Import message_space.get_all_messages
# [ ] Assign numeric ranges to each message
# [ ] Define TOTAL_RANGE
# [ ] Implement encode() and decode()
# [ ] Ensure deterministic behavior

TOTAL_RANGE = None

def encode(message):
    """
    Given a valid message, return its (low, high) numeric range.
    """
    raise NotImplementedError


def decode(value):
    """
    Given a numeric value in TOTAL_RANGE, return a valid message.
    """
    raise NotImplementedError