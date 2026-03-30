import random
import string

def password_generator(length):
    # Define character sets
    letters = string.ascii_letters
    symbols = string.punctuation
    digits = string.digits

    # Combine all characters
    all_characters = letters + symbols + digits

    password = []

    # Ensure strong password
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(symbols))
    password.append(random.choice(digits))

    # Fill remaining characters
    for i in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle and convert to string
    random.shuffle(password)
    return "".join(password)


print(" Password is generating")

length = int(input(f"Enter password length (min 4): "))

if length < 4:
    print(" Password should have at least 4 characters")
else:
    result = password_generator(length)
    print(f" Generated Password: {result}")
