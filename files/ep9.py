# ep9 - OOP
class Car:
    # attributes
    # brand = 'Toyota'
    # year = 2022
    # fuel = 50.00
    # status = True
    brand = None
    year = None
    fuel = None
    status = None
    # constructor
    def __init__(self, brand, year, fuel, status):
        print(f'this method/constructor is automatic run when {self} is created')
        self.brand = brand
        self.year = year
        self.fuel = fuel
        self.status = True
    # method
    def checkStatus(self):
        if self.status == True:
            print('This car is tested')
        else:
            print('This car is no test yet')
    def drive(self):
        print('This car is driving')
# static
class First:
    language = 'Python'
    def learn(): # static method, no need to define self
        print(f'I am learning {First.language} programming language') # static variable could access via className.variable
    def teach(self):
        First.learn()
        print(f'i could teach {self.language} programming language')

##########################
if __name__ == '__main__':
    print('-----"-----')
    car1 = Car('Volkswagen', 1987, 75, False)
    car2 = Car('Mercedes', 2000, 80, True)
    # print(type(car1))
    # print(type(car2))
    print(f'Brand: {car1.brand}')
    print(f'Brand: {car1.year}')
    print(f'Brand: {car1.fuel}')
    car1.drive()
    car1.checkStatus()
    car2.checkStatus()
    print(First.language)
    First.learn()
    first = First()
    first.teach()
