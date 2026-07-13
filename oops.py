class student: #class name
    name="lucky" #attribute
    def study(self):#reperesents current object
        print("lucky is studying")
s1 = student() #s1 is a object
print(s1.name)
s1.study()# study is a method

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

s1=student("lucky",20)
s2=student("uma",21)
print(s1.name ,s2.name)
print(s1.age ,s2.age)

class bank:
    def __init__(self,balance):
        self.balance = balance
    def check_balance(self):
        print(self.balance)
account = bank(5000)
account.check_balance()

class user:
    def __init__(self,name):
        self.name=name
    def login(self):
        print(self.name,"logged in")
u1=user("prathi")
u1.login()
u2=user("lucky")
u2.login()
    
class A:
    def show(self):
        print("Class A")

class B(A): 
    def show2(self):
        print("Class B")

b = B()
b.show()  
b.show2()  

class father:
    def house(self):
        print("house")
class son(father):
    def car(self):
        print("car")
s=son()
s.house()
s.car()

class thatta:
    def land(self):
        print("thatta's land")

class appa(thatta):
    def house(self):
        print("appa's land")

class maga(appa):
    def bike(self):
        print("son has a bike")

obj = maga()
obj.land()
obj.house()
obj.bike()
        

class appa :
    def house(self):
        print("appa's house")
class amma :
    def car(self):
        print("amma's car")
        
class maga(appa,amma):
    def bike(self):
        print("maga's bike")

firstclass = maga()
firstclass.house()
firstclass.car()
firstclass.bike()


class student:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
s=student("lucky")
print(s)

def login(fun):
    def wrapper():
        print("login")
        fun()
    return wrapper
@login
def dashboard():
    print("dashboard page")
dashboard()

def message(fun):
    def wrapper():
        print("Function started")
        fun()
        print("Function ended")
    return wrapper 
@message
def hello():
    print("Hello Python")
hello()