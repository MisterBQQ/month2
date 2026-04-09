class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Мне {self.age} лет, я работаю как {self.profession}.")

class Classmate(Person):
    def __init__(self, name, age, profession, group_name):
        super().__init__(name, age, profession)
        self.group_name = group_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я твой одногруппник из {self.group_name}. "
              f"Мне {self.age} и я будущий {self.profession}.")

class Friend(Person):
    def __init__(self, name, age, profession, hobby):
        super().__init__(name, age, profession)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я твой друг! Мне {self.age}, "
              f"работаю {self.profession}, а в свободное время обожаю {self.hobby}.")

student1 = Classmate("Али", 20, "Разработчик", "ПИ-22")
student2 = Classmate("Азамат", 19, "Дизайнер", "ГД-21")

friend1 = Friend("Данияр", 25, "Инженер", "играть в шахматы")
friend2 = Friend("Алина", 23, "Маркетолог", "фотографировать")

student1.introduce()
student2.introduce()
friend1.introduce()
friend2.introduce()
