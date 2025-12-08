import string_utils as s
import random_utils as r
import constants as c

print(s.upper("слово"))
print(s.count("привет"))
print(s.palindrome("level"))

print(r.random_number(1, 10))
print(r.random_list(4, 2, 10))

print(c.pi) # число пи
print(c.G) # гравитационная постоянная
print(c.C) # скорость света

radius = 4
print(f"S = {c.pi} * {radius} = {c.pi * radius ** 2}") # площадь окружности

m = 0.001
print(f"E = {m} * {c.C} = {m * c.C ** 2}") # формула E = mc^2