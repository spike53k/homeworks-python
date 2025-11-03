list = [2, 5, 1, -4, -5, 7, -9, 8]
list_minus = []
list_2 = []
list_3 = []
list_4 = []
result = 1

print("Список всех чисел:", list)

for i in list:
    if i < 0:
        list_minus.append(i)
print("Сумма отрицательных чисел: ")
print(sum(list_minus))

for i1 in list:
    if i1 % 2 == 0:
        list_2.append(i1)
print("Сумма четных чисел: ")
print(sum(list_2))

for i2 in list:
    if i2 % 2 != 0:
        list_3.append(i2)
print("Сумма нечетных чисел")
print(sum(list_3))

for i3 in list:
    if list.index(i3) % 3 == 0:
        list_4.append(i3)
for num in list_4:
    result *= num
print("Произведение чисел с индексами кратными трём: ")
print(result)