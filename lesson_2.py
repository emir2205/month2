class Person:
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation

    def introduce(self):
        print(f"Меня зовут {self.name}, я родился {self.birth_date}, "
              f"по профессии - {self.occupation}.")

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, group_name):
        super().__init__(name, birth_date, occupation)
        self.group_name = group_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одноклассник Байэля. "
              f"Я из группы {self.group_name}, работаю {self.occupation}.")

class Friend(Person):
    def __init__(self, name, birth_date, occupation, hobby):
        super().__init__(name, birth_date, occupation)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я друг Байэля. "
              f"Мое хобби - {self.hobby}, работаю {self.occupation}.")

classmate1 = Classmate("Эмир", "22.05.2004", "программистом", "geeks62-1")
classmate2 = Classmate("Максим", "10.01.2005", "аналитиком", "geeks62-2")
friend1 = Friend("Алмаз", "05.12.2003", "программистом", "Футбол")
friend2 = Friend("Саша", "15.06.1999", "дизайнером", "Фотография")

people_list = [classmate1, classmate2, friend1, friend2]
for person in people_list:
    person.introduce()