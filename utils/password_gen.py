import secrets
import string

def generate_password(
    length: int = 15,
    uppercase: bool = True,
    lowercase: bool = True,
    digits: bool = True,
    symbols: bool = True,
) -> str:
    """Generate a cryptographically secure password."""

    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    character_sets = []
    password = []

    if uppercase:
        character_sets.append(string.ascii_uppercase)

    if lowercase:
        character_sets.append(string.ascii_lowercase)

    if digits:
        character_sets.append(string.digits)

    if symbols:
        character_sets.append("!@#$%^&*()-_=+[]{}<>?")

    if not character_sets:
        raise ValueError("Select at least one character type.")

    # Ensure every selected type appears at least once
    for charset in character_sets:
        password.append(secrets.choice(charset))

    # Pool of all selected characters
    all_characters = "".join(character_sets)

    while len(password) < length:
        password.append(secrets.choice(all_characters))

    # Shuffle securely
    secrets.SystemRandom().shuffle(password)

    return "".join(password)




def check_strength(password: str) -> dict:
    """
    Check password strength.
    Returns a dict with score (0-5), label, and tips.
    """
    common_passwords = {
        "password",
        "123456",
        "123456789",
        "qwerty",
        "admin",
        "welcome",
        "letmein",
    }

    if password.lower() in common_passwords:
        return {
            "score": 0,
            "label": "🟥 Very Weak",
            "bar": "░░░░░",
            "tips": ["This is a commonly used password."],
        }

    score = 0
    tips = []

    # Length checks
    if len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters")

    if len(password) >= 12:
        score += 1

    if len(password) >= 16:
        score += 1

    if len(set(password)) < len(password) // 2:
        tips.append("Avoid repeating the same characters")
        score = max(score - 1, 0)

    # Character variety
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    variety = sum([has_upper, has_lower, has_digit, has_symbol])

    if variety >= 3:
        score += 1
    else:
        if not has_upper:
            tips.append("Add uppercase letters")
        if not has_lower:
            tips.append("Add lowercase letters")
        if not has_digit:
            tips.append("Add numbers")
        if not has_symbol:
            tips.append("Add special characters")

    if variety == 4:
        score += 1

    # Labels
    labels = {
    0: "🟥 Very Weak",
    1: "🟧 Weak",
    2: "🟨 Fair",
    3: "🟦 Good",
    4: "🟩 Strong",
    5: "🟢 Excellent",
    }

    bar = "█" * score + "░" * (5 - score)

    return {
    "score": score,
    "label": labels.get(score, "Unknown"),
    "bar": bar,
    "tips": tips,
    }
