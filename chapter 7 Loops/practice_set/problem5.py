#  Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter a number"))

i=1
fact=1
for i in range(1,n+1):
    fact = fact*i
    
print("Factorial is : ",fact)