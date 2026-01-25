class Human:
    def __init__(self, name, age, date, phone):
        self.name = name
        self.age = age
        self.date = date
        self.phone = phone

    def show_info(self):
        print(f"Human info \n"
              f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"Date: {self.date}\n"
              f"Phone: {self.phone}")

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age
    def set_date(self, date):
        self.date = date
    def get_phone(self):
        return self.phone
    def get_name(self):
        return self.name

Bob = Human("Боб", 20, "2020", "8900123123")
Bob.set_name("Bob")

Bob.show_info()