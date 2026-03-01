class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self._position = position

    def get_position(self):
        return self._position

    def display_info(self):
        print(f"имя: {self._name}, возраст: {self._age}, должность: {self._position}")

class Manager(Employee):
    def __init__(self, name, age, position):
        super().__init__(name, age, position)
        self._team = []

    def add_to_team(self, employee):
        if employee not in self._team:
            self._team.append(employee)
            print(f"{employee.get_name()} добавлен в команду\n")

    def display_team_info(self):
        print(f"\nкоманда {self._name}:")
        if not self._team:
            print("нет сотрудников")
        else:
            for employee in self._team:
                print(f"{employee.get_name()} ({employee.get_position()})")

e1 = Employee("Иван", 20, "программист")
e2 = Employee("Алексей", 20, "программист")

m = Manager("Кирилл", 25, "программист")

m.add_to_team(e1)
m.add_to_team(e2)

e1.display_info()
e2.display_info()


m.display_info()
m.display_team_info()