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
    def higher_education(self):
        if self.__higher_education:
            return "есть высшее образование."
        else:
            return "нет высшего образования."

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. {self.higher_education}")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):

        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Я учился с Айсулуу в группе {self.group_name}. {self.higher_education}")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Мое хобби {self.hobby}. {self.higher_education}")

cl1 = Classmate("Али", "20.02.2000", "студент", True, "11D")
cl1.introduce()

fr1 = Friend("Азамат", "20.02.2000", "студент", True, "футбол")
fr1.introduce()