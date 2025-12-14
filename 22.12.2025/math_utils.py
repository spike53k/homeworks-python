def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    f = [0, 1]
    for i in range(2, n):
        f.append(f[i - 1] + f[i - 2])
    return f

def summa(n):
    if n < 0:
        n = -n
    t = 0
    while n > 0:
        t += n % 10
        n = n // 10
    return t