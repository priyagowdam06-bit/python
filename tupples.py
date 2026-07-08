# students = ("ram","sam","bheem")
# print(students[-2])
# #########tuple is a collection used to store multiple
# numbers = (10,20,30,40)
# print(numbers [-3])

# data = (1,2,3)
# data[0] = 100

# print(data)
# x=(1,2,3,2,1,1,1)
# print(x.count(1))
# print(x.count(2))

# x = ("apple","banana","grapes","banana")
# print(x.count("banana"))

# num = (10,20,30,40,50)
# print(num[1:4])

# ###########sets#############
# ##set is a collection of : remove duplicate values

# x = {1,2,3,2,1,1,1}
# print(x)
# data = {1,2,3}
# data.add(4)
# print(data)

#########Function############

# def greeting():
#     print("hello students")
# greeting()

# def add():
#     return 10 + 20
# result = add()
# print(result)

# def sub():
#     return 20 - 10
# result = sub()
# print(result)

# def mul():
#     return 2 * 5
# result = mul()
# print(result)

# def div():
#     return 8 / 2
# result = div()
# print(result)

# def add(*numbers):
#     print(numbers)
# add(10,20,30,40,50,60)

# def priya(*numbers):
#     print(numbers)
# add(10,20,30,40,50,60)

# def add(*num):
#     total = 0
#     for i in num:
#         total +=i
#     print(total)
# add(10,20,30,40,50,60)

#########**kwargs#########

# def student(**details):
#     print("name :",details["name"])
#     print("age :",details["age"])
#     print("job:",details["job"])
# student(
#     name="priyaa",
#     age=20,
#     job="sales",
# )
# def square(x):
#     return x * x
# print(square(16))
# square = lambda x:x*x
# print(square(25))

# add = lambda a,b:a+b
# print(add(10,20))

# even_odd = lambda x:"even" if x%2 else "odd"
# print(even_odd(10))
# print(even_odd(15))

# upper = lambda x : x.upper()
# print(upper("priya"))

# length = lambda x : x.len()
# print(len("priya"))

# file = open("student.txt","w")
# file.write("hello priya")
# file.close()

# print("data written successfully")
# file = open("student.txt","r")
# data= file.read()
# print(data)
# file.close()

# file = open("student.txt","a")
# file.write("\nhello")
# file.close()

# print("Data append successfully")

# file = open("student.txt","r")
# print(file.read())
# file.close()

# try:
#     a =10
#     b =5
#     print(a/b)
# except:
#     print("something went wrong")

# try:
#     a = int(input("enter A:"))
#     b = int(input("enter b:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("enter only numbers")
# try:
#     file =open("data.txt")
#     print(file.read())
# except:
#     print("file error")
# finally:
#     print("program completed")

# try:
#     print(10/2)
# except:
#     print("error")
# else:
#     print("success")