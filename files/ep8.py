# ep8 - OOP
# basic class
# class Dog():
#     def __init__(self, name):
#         self.name = name
#     def sit(self):
#         print(self.name + ' is sitting.')

# d = Dog('Cream')
# d.sit()

# # class inheritance
# class SecurityDog(Dog):
#     def __init__(self, name):
#         super().__init__(name)
#     def skill(self, something='watching'):
#         print(self.name + f' is {something} the intruder')

# sd = SecurityDog('Creamy')
# sd.skill('barking')
# sd.sit()
# sd.skill('bitting')

g = ['Male', 'male', 'M', 'm']
class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def study(self):
        print(f'{self.name} is taking the class...')
    def hello(self):
        if self.gender in g:
            tone = 'Khrup'
        else:
            tone = 'kha'
        print(f'Hello, {tone}, my name is {self.name}')
# inheritance
class SpecialStudent(Student):
    def __init__(self, name, age, gender, parent):
        super().__init__(name, age, gender)
        self.parent = parent
        # self.person = person
    def whatsup(self, person='friend'):
        if person == 'friend':
            print(f"Hey, what's up {person}?")
        else:
            print(f"Oop! {person}! (Running away...)")
    # overide method
    def hello(self):
        print(f"what's up, my name is {self.name}")
class Teacher:
    def __init__(self, name, gender, subject):
        self.name = name
        self.gender = gender
        self.subject = subject
        # if self.gender == 'Male' or self.gender == 'male' or self.gender == 'm' or self.gender == 'M':
        if self.gender in g:
            self.pronoun = 'he'
        else:
            self.pronoun = 'she'
    def teach(self):
        print(f'{self.name} is teaching {self.subject}.')

if __name__ == '__main__': # to prevent running below lines of code while importing the module in other file
    print('\n')
    student1 = Student('John', 15, 'Male')
    student2 = Student('Jane', 14, 'Female')
    student3 = SpecialStudent('Brit', 16, 'Female', 'Director')
    student1.study()
    student1.hello()
    student2.hello()
    student3.hello()
    student3.whatsup('teacher')
    student3.whatsup()

    teacher1 = Teacher('Sara', 'Female', 'English')
    print(teacher1.name, f' is a teacher, {teacher1.pronoun} is teaching ', teacher1.subject)
    teacher1.teach()
    teacher2 = Teacher('Jame', 'Male', 'Math')
    print(teacher2.name, f' is a teacher, {teacher2.pronoun} is teaching ', teacher2.subject)
    teacher2.teach()

    print('\n')