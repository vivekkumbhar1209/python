#  Write a program to find the greatest of four numbers entered by the user. 

a = int(input("enter number 1 : "))
b = int(input("enter number 2 : "))
c = int(input("enter number 3 : "))
d = int(input("enter number 4 : "))

if(a>b and a>c and a>d):
    print(a ,"is gretest")
elif(b>a and b>c and b>d):
    print(b ,"is gretest ")
elif(c>a and c>b and c>d):
    print(c , " is gretest")
else:
    print(d," is gretest ")
