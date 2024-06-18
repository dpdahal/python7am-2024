# try:
#     print(10/0)
# except Exception as e:
#     print("Error: ", e)

# print("hello python")


def add(x,y):
    if y==0:
        raise Exception("y should not be 0")
    else:
        return x/y
    

try:
    print(add(10,0))
except Exception as e:
    print("Error: ", e)