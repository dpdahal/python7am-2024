# what is module?
# module is a file containing python definitions and statements.
#  The file name is the module name with the suffix .py appended.

# types of modules
# 1. Built-in modules
# 2. User-defined modules


# import calculator as cal

# print(calculator.add(10, 20))

# print(cal.add(10, 20))

# from calculator import add,sub

# from calculator import *

# from module.lib.calculator import add
# from module.lib.product import add as product_add


# print(add(10, 20))

# from lib.calculator import add

# print(add(10, 20))


# from lib import *

# print(calculator.add(3,4))


# import sys 
# import os
# import datetime
# import calendar

# print(calendar.month(2021, 1))



# import datetime

# created_at="2024-01-11"
# created_at = datetime.datetime.strptime(created_at, "%Y-%m-%d")
# print(created_at)
# print(datetime.datetime.now())

# today = datetime.datetime.now()
# b_date = datetime.datetime(1995, 1, 1)
# print(today - b_date)

import datetime

jobs=[
    {'title':'Software Engineer', 'company':'Google', 'exp_date':'2022-01-24'},
    {'title':'Python developer', 'company':'ms', 'exp_date':'2025-01-24'},
    {'title':'DevOps Engineer', 'company':'Amazon', 'exp_date':'2022-01-24'},
    {'title':'Data Analyst', 'company':'Facebook', 'exp_date':'2022-01-24'},
    {'title':'Data Scientist', 'company':'TCS', 'exp_date':'2024-10-24'},

]


for job in jobs:
    exp_date = datetime.datetime.strptime(job['exp_date'], "%Y-%m-%d")
    today = datetime.datetime.now()
    if exp_date < today:
        exp_days = today - exp_date
        print(f"{job['title']} job in {job['company']} is expired {exp_days.days} days ago")
    else:
        active_days = exp_date - today
        print(f"{job['title']} job in {job['company']} {active_days.days} is active")
   