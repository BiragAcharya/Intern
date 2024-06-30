#polymorphism
#method overiding

# class Shape:
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 22/7 * self.radius ** 2
    
# class Rectangle(Shape):
#     def __init__(self, length, width):
#             self.length = length
#             self.width = width
        
#     def area(self):
#             return self.length * self.width

# def print_area(x):
#      print("Area: ", x.area())

# rectangle = Rectangle(5,2)
# circle = Circle(7)

# print_area(rectangle)
# print_area(circle)



# class Animal:
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "Woof !"
    
# class Cat(Animal):
#     def speak(self):
#         return "Meow !"

# def make_sound(animal):
#     print(animal.speak())

# animals = [Dog(), Cat()]
# for animal in animals:
#     make_sound(animal)



class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 50000
    
class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return 25000
    
employees = [FullTimeEmployee('Bob'), PartTimeEmployee('Pranjal')]
for employee in employees:
    print(f"{employee.name}'s salary: ", employee.calculate_salary())




#Clint Server Architecture

#Frontend           Backend



#Monolithic Architecture
#Frontend           Backend
#html, css          django


#HTTP Satus Code( gareko kura vayo ki vayena vanne ho)

#1XX- information
#2XX - success / ok xa
#3xx - redirect
#4xx - client error
#5xx - server



#HTTP  verbs/ methods( k gareko vanne ho)

# get
# post
# delete
# put
# patch



