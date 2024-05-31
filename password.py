import re

def assess_password_strength(password):
    # Criteria checks
    length = len(password) >= 8
    has_upper = re.search(r'[A-Z]', password) is not None
    has_lower = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special = re.search(r'[\W_]', password) is not None

    # Scoring the password based on criteria
    score = sum([length, has_upper, has_lower, has_digit, has_special])
    
    # Providing feedback based on score
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    feedback = {
        "Length >= 8 characters": length,
        "Contains uppercase letters": has_upper,
        "Contains lowercase letters": has_lower,
        "Contains numbers": has_digit,
        "Contains special characters": has_special
    }

    return strength, feedback

# Get user input
password = input("Enter a password to assess its strength: ")
strength, feedback = assess_password_strength(password)

# Display results
print(f"Password Strength: {strength}")
print("Feedback:")
for criterion, met in feedback.items():
    print(f"  {criterion}: {'Yes' if met else 'No'}")
