import pyperclip


def copy(text: str):
    """Copy text to clipboard."""

    pyperclip.copy(text)