import random
import string

def Random(length):
	# Ensure the length is at least 1
    length = max(length, 1)

    # Generate a random string with letters, numbers, and underscores
    random_string = random.choice(string.ascii_letters)  # Start with a letter

    # Add the remaining characters
    for _ in range(length - 1):
        # Use string.ascii_letters + string.digits + '_' for allowed characters
        random_string += random.choice(string.ascii_letters + string.digits + '_')

    return random_string