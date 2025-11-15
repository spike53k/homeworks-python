# 1 задача
def formated_text():
    print("“Don't let the noise of others' opinions\n drown out your own inner voice.”\n\t\t\t\t\t\t\t\tSteve Jobs")
formated_text()

# 2 задача
def odd_numbers(start, end):
    for num in range(start, end):
        if num % 2 == 0:
            print(num)
odd_numbers(1, 10)

# 3 задача
def line(lenght, direction, symbol):
    if direction == "h":
        print(symbol * lenght)
    elif direction == "v":
        for i in range(lenght):
            print(symbol)
line(10, "h", "_")

# 4 задача
def max_num(n1, n2, n3, n4):
    return max(n1, n2, n3, n4)
print(max_num(1, 2, 8, 4))

# 5 задача
def sum_nums(start, end):
    list1 = []
    for num in range(start, end):
        list1.append(num)
    print(sum(list1))
sum_nums(1, 5)

# 6 задача
def simple_number(num):
    if num <= 1:
        return False
    if num == 0:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
print(simple_number(7))

# 7 задача
def lucky_number(num):
    if num < 100000 or num > 999999:
        return False
    num1 = str(num)
    first_sum = int(num1[0]) + int(num1[1]) + int(num1[2])
    second_sum = int(num1[3]) + int(num1[4]) + int(num1[5])
    return first_sum == second_sum
print(lucky_number(123420))