# ep9 - OOP
# inheritance
class One:
    name = None

    def __init__(self, name):
        self.name = name

    def walk(self):
        print('i can walk')


class Two(One):
    nickname = None

    def __init__(self, name, nickname):
        super().__init__(name)
        self.nickname = nickname

    def run(self):
        print('i can run')


class Three(One):
    def eat(self):
        print('i can eat')


class Four(Two):
    def fly(self):
        print('i can fly')

##########################
if __name__ == '__main__':
    print('-----"-----')
    three = Three('Firstname')
    print(three.name)
    three.eat()
    three.walk()
    four = Four('Firstname', 'lastname')
    print(four.name, ' ', four.nickname)
    four.walk()
    four.run()
    four.fly()
    one = One('Firstname')
    two = Two('Firstname', 'Lastname')
    print(two.name, two.nickname)
