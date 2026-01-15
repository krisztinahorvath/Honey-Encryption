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

from message_space import get_all_messages

TOTAL_RANGE = None
# Build message list deterministically
ALL_MESSAGES = get_all_messages()

if not ALL_MESSAGES:
    raise ValueError("Message space is empty. get_all_messages() must return messages.")

# We assign each message a fixed-size numeric bucket/range.
# Bigger BUCKET_SIZE => bigger TOTAL_RANGE (more room).
BUCKET_SIZE = 1000  # you can change this, but keep it constant

# TOTAL_RANGE must cover all messages
TOTAL_RANGE = len(ALL_MESSAGES) * BUCKET_SIZE

# Fast lookup for encode()
_MESSAGE_TO_INDEX = {msg: i for i, msg in enumerate(ALL_MESSAGES)}

def encode(message):
    """
    Given a valid message, return its (low, high) numeric range.
    """
    if message not in _MESSAGE_TO_INDEX:
        raise ValueError(
            "Message not in valid message space. Use one of the messages from get_all_messages()."
        )

    idx = _MESSAGE_TO_INDEX[message]
    low = idx * BUCKET_SIZE
    high = low + BUCKET_SIZE
    return low, high


def decode(value):
    """
    Given a numeric value in TOTAL_RANGE, return a valid message.
    """
    if not isinstance(value, int):
        raise TypeError("value must be an integer")

    # Force value into valid domain (safe even if caller passes outside range)
    value = value % TOTAL_RANGE

    idx = value // BUCKET_SIZE
    return ALL_MESSAGES[idx]