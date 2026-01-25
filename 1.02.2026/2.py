import random

class City:
    def __init__(self, name, region, country, population):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
    def show_info(self):
        print(f"Информация о городе {self.name}")
        print("Регион:", self.region)
        print("Страна:", self.country)
        print("Население:", self.population)
city1 = City("Шелехов", "Иркутская область", "Россия", 50000)
city2 = City("Иркутск", "Иркутская область", "Россия", 650000)
city1.show_info()
city2.show_info()

exaples_city = ["Москва", "Париж", "Люксембург", "Пекин"]
exaples_region = ["Московская область", "Ленинградская область", "Красноярский край"]
exaples_country = ["Китай", "США", "Франция", "Испания"]

cities = [city1, city2]

for i in range(98):
    city = City(random.choice(exaples_city),
                random.choice(exaples_region),
                random.choice(exaples_country),
                random.randint(100000, 4000000))
    cities.append(city)
for city in cities:
    city.show_info()
    print()