#  Write a python function which converts inches to cms. 

def log(inch):
    return inch* 2.54

n = int(input("Enter value of inches :"))
print("the corresponding value in cms is", log(n))
