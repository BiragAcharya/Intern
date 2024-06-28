# detail hiding = abstraction
# data hiding = encapsulation

# __ (double underscore garera private parinxa python ma    =  Encapsulation) within the class

# _ (single underscore garera protected parinxa python ma    =  Encapsulation) within class or inherited class

#Encapsulation
# class Animal:
#     def __init__(self,name):
#         print("Constructor invoked")
#         self.name=name

#     def eat(self):
#         print(self.name)
#         print("I can eat")
    
#     def sleep(self):
#         print("I can sleep")

# class Dog(Animal):
#     def bark(self):
#         print("I can bark")
    
# dog1 = Dog('German Sephard')
# print(dog1.name)
# dog1.eat()
# dog1.sleep()


# class BankAccount:
#     def __init__(self, account_number, balance):
#         self._account_number = account_number
#         self._balance = balance

#     def deposit(self, amount):
#         self._balance += amount
#         print(f"Deposit successful. New Balance : ${self._balance}")

#     def check_balance(self):
#         print(f"Current Balance : {self._balance}")

#     def withdraw(self , amount):
#         self._balance -= amount
#         print(f"Withdraw successful. New Balance : ${self._balance}")


# account = BankAccount("1234",1000)
# account.deposit(-100)
# account.withdraw(1500)
# account.check_balance()

# print(account._account_number)


# class Employee:
#     def __init__(self, name, emp_id, salary):
#         self._name = name
#         self._emp_id = emp_id
#         self._salary = salary

#     def calaulate_bonus(self):
#         return self._salary * 0.1
    
#     def display_info(self):
#         print(f"Name: {self._name}")
#         print(f"Employee Id: ${self._emp_id}")
#         print(f"Salary: ${self._salary}")

# employee = Employee('Bob', 1, 1000)
# employee.display_info()
# bonus = employee.calaulate_bonus()

# print(bonus)


#Father    child = Ram, Hari

# class Father:
#     def talk(self):
#         print("I can talk")

# class Ram(Father):
#     pass

# class Hari(Father):
#     pass

# ram = Ram()
# ram.talk()

# hari = Hari()
# hari.talk()


class Employee:
    def __init__(self, name, emp_id):
        self.name= name
        self.emp_id= emp_id

    def display_info(self):
        print(f'Name: {self.name}')
        print(f'Employee Id: {self.emp_id}')
    
class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f'Department: {self.department}')

class Developer(Employee):
    def __init__(self, name, emp_id, programming_lang):
        super().__init__(name, emp_id)
        self.programming_lang = programming_lang

    def display_info(self):
        super().display_info()
        print(f'Programming Language: {self.programming_lang}')

manager = Developer('Bob', 1, "Engineering")
manager.display_info()
print("\n")
developer = Developer('Marley', 2, "Javascript")
developer.display_info()
        