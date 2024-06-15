import random
import string

def passgen(length=26):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_chars = lower + upper + digits + symbols
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

print("Generated password:", passgen())
