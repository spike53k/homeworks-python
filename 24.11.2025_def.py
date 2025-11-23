import random

def make_password(length):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "_-.,*"
    chars = letters + digits + letters2 + symbols
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password

def check_password(password):
    if len(password) < 6:
        return "слабая"
    elif len(password) < 10:
        return "средняя"
    else:
        return "сильная"

def make_passwords(count, length):
    passwords = []
    while len(passwords) < count:
        password1 = make_password(length)
        if password1 not in passwords:
            passwords.append(password1)
    return passwords

pass1 = make_password(8)
pass2 = make_passwords(3, 7)
print("Пароль:", pass1)
print("Надежность:", check_password(pass1))
print("Три пароля:")
print(*pass2, sep="\n")