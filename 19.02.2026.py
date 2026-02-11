def f_max(a):
    if len(a) == 1:
        return a[0]
    max_r = f_max(a[1:])
    if a[0] > max_r:
        return a[0]
    else:
        return max_r
numbers = [3, 67, 2, 9, 1]
print(f_max(numbers))


def num(n, c=[]):
    if n == 0:
        print(c)
        return
    s = 1
    if c:
        s = c[-1]
    for i in range(s, n + 1):
        num(n - i, c + [i])
num(4)