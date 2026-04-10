class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print(f"{self.get_name()}: гав, Израиль наш манипулятор!")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.get_name()}: мяу, Америка наша собака!")

dog = Dog("Дональд Трамп", 72)
cat = Cat("Бенджамин Нетаньяху", 70)

dog.make_sound()
cat.make_sound()

cat.set_age(70)
print(cat.get_age())