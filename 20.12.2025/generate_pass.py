import random

def generate():
    letters1 = "abcdefghijklmnopqrstuvwxyz"
    letters2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*"

    chars = letters1 + letters2 + numbers + symbols

    password = ""
    for i in range(10):
        password += random.choice(chars)
    return password

def test(password):
    if len(password) < 8:
        return "слабый"
    elif len(password) >= 12:
        return "хороший"
    else:
        return "средний"

def generate_passwords(n):
    passwords = []

    while len(passwords) < n:
        p = generate()
        if p not in passwords:
            passwords.append(p)
    return passwords