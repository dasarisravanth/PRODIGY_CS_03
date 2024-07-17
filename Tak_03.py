import re

def assess_password_strength(password):
    """
    Assess the strength of a password based on length, presence of uppercase and lowercase letters,
    numbers, and special characters.

    Args:
        password (str): The password to assess.

    Returns:
        str: Feedback on the password's strength.
    """
    # Criteria checks
    length_check = len(password) >= 8
    uppercase_check = re.search(r"[A-Z]", password) is not None
    lowercase_check = re.search(r"[a-z]", password) is not None
    number_check = re.search(r"[0-9]", password) is not None
    special_char_check = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None
    
    # Strength assessment
    score = sum([length_check, uppercase_check, lowercase_check, number_check, special_char_check])

    # Feedback
    if score == 5:
        return "Password strength: Very Strong"
    elif score == 4:
        return "Password strength: Strong"
    elif score == 3:
        return "Password strength: Medium"
    elif score == 2:
        return "Password strength: Weak"
    else:
        return "Password strength: Very Weak"

def main():
    while True:
        password = input("Enter a password to assess its strength: ")
        feedback = assess_password_strength(password)
        print(feedback)

        cont = input("Do you want to assess another password? (y/n): ").lower()
        if cont != 'y':
            break

if __name__ == "__main__":
    main()
