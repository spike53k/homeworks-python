list = [1, 4, 3, 9, 7, 0, 3, 2, -2, -4]

print("весь список:", *list)

countminus = 0
countplus = 0
countzero = 0

print("минимальное число в списке:", min(list))
print("максимальное число в списке:", max(list))

for num in list:
    if num < 0:
        countminus += 1
print("количество отрицательных чисел:", countminus)

for num1 in list:
    if num1 > 0:
        countplus += 1
print("количество положительных чисел:", countplus)

for num2 in list:
    if num2 == 0:
        countzero += 1
print("количество нулей:", countzero)