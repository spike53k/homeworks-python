math_students = {"Анна", "Борис", "Виктор", "Дарья", "Елена"}
physics_students = {"Виктор", "Георгий", "Дарья", "Иван", "Ксения"}
cs_students = {"Анна", "Виктор", "Елена", "Иван", "Мария"}

# студенты которые посещают все три курса
excelent_students = math_students.intersection(physics_students, cs_students)
print(excelent_students)

# студенты которые посещают только математику
only_math_students = math_students.difference(physics_students, cs_students)
print(only_math_students)

# все уникальные студенты которые посещают только один предмет
unic_math = math_students.difference(physics_students, cs_students)
unic_physics = physics_students.difference(math_students, cs_students)
unic_cs = cs_students.difference(math_students, physics_students)
print(unic_math, unic_physics, unic_cs)

# студенты которые посещают ровно два курса
math_physics = (math_students & physics_students) - cs_students
math_cs = (math_students & cs_students) - physics_students
cs_physics = (cs_students & physics_students) - math_students
print(math_physics, math_cs, cs_physics)