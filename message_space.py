"""
Defines the message space used by the Honey Encryption system.

This file should:
- Define a structured and finite set of valid messages (e.g., meeting messages).
- Enumerate all possible messages deterministically.
- Expose a list or function that returns all valid messages.

This message space represents the distribution over which the
Distribution-Transforming Encoder (DTE) operates.
"""

# TODO:
# [ ] Choose message domain (e.g., meeting messages)
# [ ] Define fixed templates
# [ ] Enumerate all valid messages deterministically
# [ ] Expose ALL_MESSAGES as a list of strings

def get_all_messages():
    """
    Return a list of all valid plaintext messages.
    """
    # Domain pieces (keep small/finite but plausible)
    actions = [
        "Meeting",
        "Lunch",
        "Study session",
        "Project sync",
        "Coffee",
        "Call",
    ]

    times = [
        "8am", "9am", "10am", "11am",
        "12pm", "1pm", "2pm", "3pm", "4pm", "5pm",
    ]

    places = [
        "near library",
        "in cafeteria",
        "at main hall",
        "by the fountain",
        "in room 101",
        "in room 202",
        "at the lab",
        "at the park",
    ]

    # Deterministic enumeration (fixed nesting order)
    messages = []
    for act in actions:
        for t in times:
            for p in places:
                messages.append(f"{act} at {t} {p}")

    return messages
