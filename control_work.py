class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            print("Возраст должен быть положительным!")

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"

class Cat(Animal):
    def make_sound(self):
        return "Мяу!"

dog = Dog("Шарик", 3)
cat = Cat("Барсик", 2)

print(f"{dog.name} говорит: {dog.make_sound()}")
print(f"{cat.name} говорит: {cat.make_sound()}")

print(f"Старый возраст собаки: {dog.age}")
dog.age = 6
print(f"Новый возраст собаки: {dog.age}")
dog.name = "Кекс"
print(f"Новое имя собаки: {dog.name}")