# def total(x,y):
#     print(x+y)


# total(10,20)


# def message(times):
#     for x in range(times):
#         print("Hi")

# message(5)

# def even_odd(num) and print even or odd

# def enve_odd(num):
#     if num%2==0:
#         print("Even")
#     else:
#         print("Odd")

# n=int(input("Enter a number: "))
# enve_odd(n)
# def function multipication table

# def mul(num):
#     for x in range(1,11):
#         print(num,"*",x,"=",num*x)  


# n=int(input("Enter a number: "))
# mul(n)

# def user_info(name,email,address):
#     print("Name: ",name)
#     print("Email: ",email)
#     print("Address: ",address)


# name = input("Enter your name: ")
# email = input("Enter your email: ")
# address = input("Enter your address: ")
# user_info(name,email,address)

# def students(name,nep,eng,mat,sic,com):
#     total = nep+eng+mat+sic+com
#     per = total/5
#     print("Name: ",name)
#     print("Total: ",total)
#     print("Percentage: ",per)
#     if per>35 and per<45:
#         print("C Grade")
#     elif per>45 and per<60:
#         print("B Grade")
#     elif per>60 and per<75:
#         print("A Grade")
#     elif per>75:
#         print("A+ Grade")
#     else:
#         print("Fail")

# name = input("Enter your name: ")
# nep = int(input("Enter Nepali marks: "))
# eng = int(input("Enter English marks: "))
# mat = int(input("Enter Math marks: "))
# sic = int(input("Enter Science marks: "))
# com = int(input("Enter Computer marks: "))
# students(name,nep,eng,mat,sic,com)


# define function
# def introduction():
#     # function body 
#     print("Hello, I am a function")

# # calling function
# introduction()

# function with parameter


# def introduction(name,age):
#     print(f"Hello, I am {name} age {age} years old.")

# introduction('ram',20)
# introduction('shyam',40)


# optional parameter

# a=1
# a=50

# def introduction(name,phone,age=0):
#     print(f"Hello, I am {name} age {age} years old.")

# introduction('ram',98987,20)


# def users(names):
#     print(names)


# users(['ram','shyam','hari'])

# *args-> array arguments
# **kwargs-> keyword dictionary arguments
# def add(x,y):
#     print(x+y)

# add(10,20)

# def users(*args,**kwargs):
#     print(args)
#     print(kwargs)


# users('ram','shyam','hari',name='sophia',age=20)

# data=['ram',20]

# data={
#     'name':'ram',
#     'age':20
# }

# def total(*numbers):
#     sm=0
#     t =len(numbers)
#     for num in numbers:
#         sm+=num

#     print("Total: ",sm)
#     print("per: ",sm/t)


# total(10,20,67,87,78)


# function return value

# def add(x,y):
#     t= x+y
#     return t 
#     return x-y

# sm = add
# print(sm)
# print(add(10,20))

# a =5
# b=6
# # print(a+b)
# c=a+b
# print(c)


# function scope
# global scope
# local scope

# def test():    
#     x=5

   
# test()

# print(x)


# a=5

# def test():
#     global a
#     a=a+30
#     print(a)

# test()
# print(a)


# def add(x,y):
#     return x+y

# # print(add)

# total =add
# print(total(10,20))


# def add(x,y):
#     return x+y


# def total():
#     print(add(20,50))

# total()



def take_value():
    p =int(input("Enter principal amount: "))
    r =int(input("Enter rate of interest: "))
    t =int(input("Enter time: "))
    return [p,r,t]


def calculate():
    p,t,r = take_value()
    return p*t*r/100

def display():
    print("Simple interest: ",calculate())

display()


# define function to take any word and check total vowel and consonant
# course ="we are learning python"

# module
# package
# function document
