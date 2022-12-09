import random

# Set the length of the password
password_length = 8

# Use the string of lowercase letters, uppercase letters, digits, and punctuation marks to create the password
password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{};':\",.<>/?\\|"

# Generate a random password
password = "".join(random.choices(password_chars, k=password_length))

# Print the password
print(password)
