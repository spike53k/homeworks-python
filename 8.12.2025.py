# задача 1
list1 = [1, 2, 3, 4]
try:
    total = sum(list1)
    print(total)
except TypeError as e:
    print("ошибка: в списке есть не числовое значение")

# задача 2
list2 = [1, 2, 3, 0, 5]

try:
    d = int(input("введите делитель: "))

    if d == 0:
        print("ошибка: деление на ноль невозможно")
    else:
        print("результаты деления:")
        for n in list2:
            print(n / d)

except ValueError:
    print("ошибка: введено не число")
except ZeroDivisionError:
    print("ошибка: делить на ноль нельзя")
except Exception as e:
    print(f"произошла ошибка: {e}")


# задача 3
nums = []
try:
    if not nums:
        raise ValueError("список пустой")
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    print(nums)
    print(max_num)

except ValueError as e:
    print(f"ошибка: {e}")
except Exception as e:
    print(f"произошла непредвиденная ошибка: {e}")