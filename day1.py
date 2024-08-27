#camelCase  ------javascript
# PascalCase  ------- Java
# kebab-case ------
# snake_case ------  Python


# """""""""""""""""""""""""""""""""""""""""""""""
#pathaune argument
#liney parameter


# hello={
#     "name": "Ram",
#     "age":22,
#     "roll":23
# }
# hello["isIIC"] = "Itahari"
# print(hello)

# del hello["age"]
# print(hello)

# print(hello.keys())
# print(hello.values())

# if 'name' in hello:
#     print("I am here")



# tuplee = (2,3,4,"Birag",2)
# tuplee[0] = 'Ram'
# tuple ho change hudaina so immutable




# double == vaneko condition check ,,,,  triple === vaneko condition check + datatype

# fruits= ['apple', 'banana', 'mango']
# for fruit in fruits:
#     print(fruit)

# colors= ['red', 'green', 'yellow']
# for color in colors:
#     print(color)

# unique_numbers={1,2,3,4,5}
# for number in unique_numbers:
#     print(number)



grades={
    "Ram":90,
    "bob":88,
    "Taylor":99
}
print(grades.values())

print(grades.items())

print(grades["Ram"])

for student in grades:
    print(student,"scored",grades[student])

for student,grade in grades.items():
    print(student,"scored",grades[student])

for value in grades.values():
    print(value)
    

message = "This much for today!"
for char in message:
    print(char)
