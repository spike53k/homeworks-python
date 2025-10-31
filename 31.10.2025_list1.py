primer = input("введите арифметическое выражение например 23+12: ")

if "+" in primer:
    num1, num2 = primer.split("+")
    result = int(num1) + int(num2)
elif "-" in primer:
    num1, num2 = primer.split("-")
    result = int(num1) - int(num2)
elif "*" in primer:
    num1, num2 = primer.split("*")
    result = int(num1) * int(num2)
elif "/" in primer:
    num1, num2 = primer.split("/")
    result = int(num1) / int(num2)
print("Результат: ", result)