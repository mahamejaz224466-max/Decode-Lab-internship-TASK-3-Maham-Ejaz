
# Project 3: Enterprise Random Password Generator

import secrets
import string
import math

MIN_LENGTH = 8
RECOMMENDED_LENGTH = 15


def get_password_length():

    while True:
        raw = input(f"Enter your password length (minimum {MIN_LENGTH}): ").strip()
        try:
            length = int(raw)
        except ValueError:
            print(f"'{raw}' isn't a whole number. Try again.\n")
            continue

        if length < MIN_LENGTH:
            print(f"Length must be at least {MIN_LENGTH}. Try again.\n")
            continue

        if length < RECOMMENDED_LENGTH:
            print(f"Note: NIST recommends {RECOMMENDED_LENGTH}+ characters "
                  f"for high-security accounts, but {length} will work.\n")

        return length


def generate_password(length):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_characters = lowercase + uppercase + digits + symbols

    required = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]

    remaining_count = length - len(required)
    remaining = [secrets.choice(all_characters) for _ in range(remaining_count)]

    password_chars = required + remaining


    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

    return "".join(password_chars)


def calculate_entropy(length, pool_size=94):

    return length * math.log2(pool_size)


def show_result(password, length):

    entropy = calculate_entropy(length)
    print("\nGENERATED PASSWORD:")
    print(password)

    print(f"Length: {length} characters")
    print(f"Estimated entropy: {entropy:.1f} bits")
    if entropy >= 80:
        print("Strength: Excellent")
    elif entropy >= 60:
        print("Strength: Good")
    else:
        print("Strength: Weak")
    print()


def main():
    print("-" * 42)
    print("   ENTERPRISE RANDOM PASSWORD GENERATOR")
    print("-" * 42)

    while True:
        length = get_password_length()
        password = generate_password(length)
        show_result(password, length)

        again = input("Generate another password? (y/n): ").strip().lower()
        if again != "y":
            print("Thnak You")
            break


if __name__ == "__main__":
    main()
