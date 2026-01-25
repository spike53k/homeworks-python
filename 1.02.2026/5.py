class Country:
    def __init__(self, name, continent, people, code, capital, cities):
        self.name = name
        self.continent = continent
        self.people = people
        self.code = code
        self.capital = capital
        self.cities = cities

    def show_info(self):
        print(f"Информация о {self.name}\n"
              f"Континент: {self.continent}\n"
              f"Население: {self.people}\n"
              f"Телефонный код: {self.code}\n"
              f"Столица: {self.capital}\n"
              f"Города: {self.cities}")

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_people(self):
        return self.people

    def set_people(self, people):
        self.people = people

    def get_capital(self):
        return self.capital

russia = Country("Россия", "Евразия", 140000, 777, "Москва", ["Иркутск", "Ангарск", "Шелехов"])
russia.show_info()