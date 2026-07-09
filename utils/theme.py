from rich.console import Console

THEME = "\033[96m"

THEMES = {
    "default": "\033[96m",
    "blue": "\033[94m",
    "green": "\033[92m",
    "red": "\033[91m",
    "purple": "\033[95m",
    "yellow": "\033[93m",
}

RESET = "\033[0m"


def set_theme(name):
    global THEME
    THEME = THEMES.get(name, THEMES["default"])


def get_theme():
    return THEME