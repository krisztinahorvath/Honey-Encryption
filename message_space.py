"""
Defines the message space used by the Honey Encryption system.

This message space represents the distribution over which the
Distribution-Transforming Encoder (DTE) operates.
"""


def get_all_messages():
    """
    Return a list of all valid plaintext messages.
    """
    # Domain pieces
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

    # Deterministic enumeration
    messages = []
    for act in actions:
        for t in times:
            for p in places:
                messages.append(f"{act} at {t} {p}")

    return messages
