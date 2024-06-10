# x=100
# y=20

# print(x>y)

# if x>y:
#     print("x is greater than y")
# elif x==y:
#     print("x and y are equal")
# else:
#     print("y is greater than x")


# 18-40 eligible for voting

# age=int(input("Enter your age: ")) 

# if age<18:
#     print("you are child")
# elif age>=18 and age<=40:
#     print("you are eligible for voting")
# else:
#     print("you are old")


# x=10
# y=20
# z=30

# if x>y and x>z:
#     print("x is greater")
# elif y>x and y>z:
#     print("y is greater")

# else:
#     print("z is greater")


# nep,eng,math,sci,soc
# total,percentage,
# grade: 35-34 c, 45-59 b, 60-74 a, 75-100 a+

# nep=int(input("Enter nepali marks: "))
# eng=int(input("Enter english marks: "))
# math=int(input("Enter math marks: "))
# sci=int(input("Enter science marks: "))
# soc=int(input("Enter social marks: "))
# total = nep+eng+math+sci+soc
# per = total/5

# if per>=35 and per<=44:
#     print("C")
# elif per>=45 and per<=59:
#     print("B")
# elif per>=60 and per<=74:
#     print("A")
# elif per>=75 and per<=100:
#     print("A+")
# else:
#     print("Fail")


# num =15

# if num%2==0:
#     print("Even")
# else:
#     print("Odd")

# WAP to enter any number and check whether 
# it is divisible by 3 and 5 or not

# if num%3==0 and num%5==0:
#     print("Divisible by 3 and 5")
# else:
#     print("Not divisible by 3 and 5")


# nested if



# x=10
# y=20
# z=30

# if x>y:
#     if x>z:
#         print("x is greater")
#     else:
#         print("z is greater")
# else:
#     if y>z:
#         print("y is greater")
#     else:
#         print("z is greater")

# if x>y and x>z:
#     print("x is greater")
# elif y>x and y>z:
#     print("y is greater")

# else:
#     print("z is greater")


# print("==============ATM=============")
# pin = int(input("Enter your pin: "))

# if pin==1234:
#     amount=10000
#     print("1. Withdraw")
#     print("2. Balance Inquiry")
#     option = int(input("Enter your option: "))
#     if option==1:
#         namount=int(input("Enter amount to withdraw: "))
#         if namount<=amount:
#             rem=amount-namount
#             print("Withdraw Amount",namount)
#             print("Remaining balance",rem)
#         else:
#             print("Insufficient balance")
#     elif option==2:
#         print("Your balance is: ",amount)
#     else:
#         print("Invalid option")
# else:
#     print("Invalid pin")


# username ='admin5'
# password='admin4'

# if username=='admin':
#     if password=='admin':
#         print("Login success")
#     else:
#         print("Invalid password")
# else:
#     print("Invalid username")