# def greet(name):
#     print(f"Hello,{name}")

# greet("Anup")
# greet("Bob")

# def calculate(a,b):
#     sum  = a+b
#     diff = a-b
#     print(f"The sum is", sum)
#     print(f"The diff is",diff)

# calculate(4,2)


# def add_numbers(n1, n2):
#     return n1 + n2

# result = add_numbers(3,3)
# print("The sum is",result)




# add = lambda a,b : a+b
# multiply= lambda x,y : x*y

# print(add(1,2))
# print(multiply(2,3))


#dherai wata parameter huda kheri use hunxa

# def test(*args):
#     print(args)

# test(1,2,3)



# def is_odd(number):
#     return number % 2 != 0

# result = is_odd(5)
# print(result)


#WAP loop liat coming in parameter and return it

# def loops(loop):
#     for i in loop:
#         print(i)
# loops([1,2,3,4,5,6])


# print("Cube sahit:")
# x = [1,2,3,4,5,6]

# def cube_loop(cube):
#     for i in cube:
#         # print(i*i*i)
#         print(i**3)

# cube_loop(x)



# print("OOP")

# class Calculation:
#     def add(self,a,b):
#         return a+b
    
#     def subtract(self,a,b):
#         return a-b

#     def multiply(self,a,b):
#         return a*b
    
# calculator = Calculation()
# result1 = calculator.add(5,2)
# result2 = calculator.subtract(5,2)
# result3 = calculator.multiply(5,2)
# print(result1)
# print(result2)
# print(result3)




print("Last Task")
class Lasttask:
    def __init__(self, loop):
        self.loop = loop

    def list(self):
        for i in loop:
            print(i)
    
    def cubeList(self):
        for i in loop:
            print(i**3)

loop = [1,2,3,4,5]
loops = Lasttask(loop)

print( "For List:")

loops.list()
print("\n")
print("For Cube:")
loops.cubeList()

