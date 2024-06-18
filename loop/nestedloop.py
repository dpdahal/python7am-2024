# for x in range(10):
#     print("x:", x)


# data=[]

# data.append("ram")
# data.append("shyam")

# print(data)

# students=[]
# num =int(input("Enter number of students:"))

# for i in range(num):
#     name=input("Enter student name:")
#     students.append(name)


# print(students)


# WAP enter number of values and calculate sum of all values

# numbers=[]
# num=int(input("Enter number of data:"))

# for i in range(num):
#     number=int(input("Enter number:"))
#     numbers.append(number)


# total=0
# for i in numbers:
#     total+=i

# print("Total:", total)

# num = int(input("Enter number of studnets: "))
# x =1
# total_marks=[]
# while x<=num:
#     print(f"==========Student: {x}==========")
#     # print("==========Student: ",x,"==========")
#     for a in range(1):
#         nep = int(input("Enter nepali marks: "))
#         eng = int(input("Enter english marks: "))
#         math = int(input("Enter math marks: "))
#         sci = int(input("Enter science marks: "))
#         social = int(input("Enter social marks: "))
#         total = nep+eng+math+sci+social
#         total_marks.append(total)
#     x+=1
    
# for total in total_marks:
#     per = total/5
#     grade = ""
#     if per>35 and per<=45:
#         grade="C"
#     elif per>45 and per<=60:
#         grade="B"
#     elif per>60 and per<=75:
#         grade="A"
#     elif per>75 and per<=100:
#         grade="A+"
#     else:
#         grade="Fail"
#     print(f"Total Marks: {total} Percentage: {per} Grade: {grade}")



# WAP to enter number of data

#  5
#  34,34,65,56,56



# users=[
#     {'name':'ram','gender':'male','status':True},
#     {'name':'gopal','gender':'male','status':False},
#     {'name':'sophia','gender':'female','status':True},
#     {'name':'hari','gender':'male','status':True},
#     {'name':'sita','gender':'female','status':False},
#     {'name':'laxmi','gender':'female','status':False},

# ]

# total_user=len(users)
# total_male=0
# total_female=0
# total_active=0
# total_inactive=0
# total_active_male=0
# total_inactive_male=0
# total_active_female=0
# total_inactive_female=0

# for user in users:
#     if user['gender']=='male':
#         if user['status']==True:
#             total_active_male+=1
#         else:
#             total_inactive_male+=1
#         total_male+=1
#     else:
#         if user['status']==True:
#             total_active_female+=1
#         else:
#             total_inactive_female+=1
#         total_female+=1


# print(f"Total Users: {total_user}")
# print(f"Total male:{total_male}")
# print(f"Total female:{total_female}")
# print(f"Total active male:{total_active_male}")
# print(f"Total inactive male :{total_inactive_male}")
# print(f"Total active female:{total_inactive_female}")
# print(f"Total inactive female:{total_inactive_female}")


# neste loop

# *
# **
# ***
# ****
# *****


# for i in range(6,1,-1):
#     for j in range(i):
#         print("*",end="")
#     print()


#  *****
#  *moon*
#  ***
#  **
#  *
#  *
#  **
#  ***
#  *sun*
#  *****


# break
# continue

# for x in range(1,11):
#     if x==5:
#         break
#     print(x)


# for x in range(1,11):
#     if x==5 or x==7:
#         continue
#     print(x)


# function
# types of function
# 1. built-in function: len,dir,print,input
# 2. user-defined function


# print('ram')
# name ='ram'

# if()
# loop()
# function()
# oop
