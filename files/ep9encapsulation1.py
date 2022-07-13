# ep9 - OOP
# encapsulation
class BankAccount:
    def __init__(self, name, age, amount):
        self.name = name
        self._age = age  # protected
        self.__amount = amount  # private

    def showMassage(self):
        print('account acquiring')

    def _deposit(self, deposit):
        self.__amount += deposit
        print(f'add: {deposit}, total: {self.__amount}')

    def __withdraw(self, withdraw):
        self.__amount - +withdraw
        print(f'withdraw: {withdraw}, balance: {self.__amount}')

    # property type 2
    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount = amount


class Employee(BankAccount):
    def __init__(self, name, age, amount):
        super().__init__(name, age, amount)


##########################
if __name__ == '__main__':
    print('-----"-----')
    employee1 = Employee('Employee1', 20, 100000)
    print(employee1.name, employee1._age)
    # print(employee1.__amount) # could not access directly private variable
    print(employee1.amount) # access private variable through properties
    employee1.showMassage()
    employee1._deposit(50000)
    # employee1.__withdraw(25000) # could not access directly private method
    employee1.amount = 200000
    print(employee1.amount)
