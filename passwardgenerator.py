import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_special=True):
    # Define the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_numbers else ''
    special = string.punctuation if use_special else ''

    # Combine all selected character sets
    all_characters = lower + upper + digits + special

    # Ensure at least one character from each selected category is included
    password = []
    if use_uppercase:
        password.append(random.choice(upper))
    if use_numbers:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special))
    
    # Fill the remaining length with random choices from all characters
    password += random.choices(all_characters, k=length - len(password))

    # Shuffle the result to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    
    # Prompt user for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 6): "))
            if length <6:
                print("Password length should be at least 6.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Ask user for complexity options
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    # Generate the password
    password = generate_password(length, use_uppercase, use_numbers, use_special)
    
    # Display the password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
