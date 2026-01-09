class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def edu_status(self):
        if self.__higher_education:
            return "есть"
        else:
            return "нет"

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"У меня {self.edu_status} высшее образование.")

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Я учился с Айсулуу в группе {self.group_name}. "
              f"У меня {self.edu_status} высшее образование.")

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Мое хобби {self.hobby}. У меня {self.edu_status} высшее образование.")

cl1 = Classmate("Иван", "20.02.2000", "студент", True, "11D")
cl1.introduce()

fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")
fr1.introduce()