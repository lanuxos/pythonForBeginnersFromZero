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
    # property type 1

    def getAmount(self):
        return self.__amount

    def setAmount(self, amount):
        self.__amount = amount
    data = property(getAmount, setAmount)


class Employee(BankAccount):
    def __init__(self, name, age, amount):
        super().__init__(name, age, amount)


##########################
if __name__ == '__main__':
    print('-----"-----')
    employee1 = Employee('Employee1', 20, 100000)
    print(employee1.name, employee1._age)
    # print(employee1.__amount) # could not access directly private variable
    print(employee1.data) # access private variable through properties
    employee1.showMassage()
    employee1._deposit(50000)
    # employee1.__withdraw(25000) # could not access directly private method
    employee1.data = 200000
    print(employee1.data)
