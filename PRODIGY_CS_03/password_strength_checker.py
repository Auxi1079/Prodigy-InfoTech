import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Make the password at least 8 characters long.")

    # Check for lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters (a-z).")

    # Check for uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters (A-Z).")

    # Check for digits
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Include at least one number (0-9).")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Include special characters (!@#$ etc).")

    # Determine strength
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, suggestions


def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ").strip()

    strength, tips = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")

    if tips:
        print("Suggestions to improve your password:")
        for tip in tips:
            print(f"• {tip}")

if __name__ == "__main__":
    main()
