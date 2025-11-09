def sort_numbers(numbers):
    nums = numbers.split()
    nums.sort()
    return ' '.join(nums)
print(sort_numbers("7 9 3 5 -6 -2"))