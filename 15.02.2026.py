class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} говорит: {self.sound}")

    def eat(self):
        print(f"{self.name} кушает")

    def show_info(self):
        return (f"Имя: {self.name}\n"
                f"Возраст: {self.age}")

class Monkey(Animal):
    def __init__(self, name, age, sound, action):
        super().__init__(name, age, sound)
        self.action = action

    def make_action(self):
        print(f"{self.name} {self.action}")

class Lion(Animal):
    def __init__(self, name, age, sound, action):
        super().__init__(name, age, sound)
        self.action = action

    def make_action(self):
        print(f"{self.name} {self.action}")

m1 = Monkey("Обезьяна", 10, "Уа-а-а", "прыгает по деревьям")
m1.make_sound()
m1.eat()
m1.make_action()
print(m1.show_info())

print()

l1 = Lion("Лев", 15, "Рррр!", "охотится")
l1.make_sound()
l1.eat()
l1.make_action()
print(l1.show_info())