class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        if self.higher_education:
            education_status = "есть"
        else:
            education_status = "нет"

        print(
            f"Меня зовут {self.name}, я родился {self.birth_date}, "
            f"по профессии - {self.occupation}, высшего образования {education_status}."
        )


person1 = Person("Эмир", "22.05.2004", "Программист", False)
person2 = Person("Иван", "05.03.2001", "Художник", True)
person3 = Person("Анна", "14.09.2005", "Дизайнер", False)

print(person1.name, person1.birth_date, person1.occupation, person1.higher_education)
print(person2.name, person2.birth_date, person2.occupation, person2.higher_education)
print(person3.name, person3.birth_date, person3.occupation, person3.higher_education)

person1.introduce()
person2.introduce()
person3.introduce()