import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    characters = string.ascii_lowercase  # always include lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password

def get_user_input():
    length = int(input("Enter password length: "))
    
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    return length, use_upper, use_digits, use_symbols

def main():
    print("=== Password Generator ===")
    
    length, use_upper, use_digits, use_symbols = get_user_input()
    
    password = generate_password(length, use_upper, use_digits, use_symbols)
    
    print("\nGenerated Password:", password)


if __name__ == "__main__":
    main()
    
    