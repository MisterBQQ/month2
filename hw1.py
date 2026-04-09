class Person:
    def __init__(self, name, birth_date, occupation, higher_education ):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

        if self.higher_education:
            self.higher_education = "есть"
        else:
            self.higher_education = 'нету'

    def introduce(self):
        print(f'Меня зовут {self.name}, родился {self.birth_date}, профессия {self.occupation}, высшее образование {self.higher_education}')

person1 = Person('Бекхан','31.03.2010','студент',False)
person2 = Person('незнакомый','04.02.1994','инженер',True)

person1.introduce()
person2.introduce()
