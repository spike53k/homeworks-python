import random

def random_number(a, b):
    return random.randint(a, b)
def random_list(n, a, b):
    result = []
    for i in range(n):
        result.append(random_number(a, b))
    return result