# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.


a = int(input("Enter mark of java :"))
b = int(input("Enter mark of C :"))
c = int(input("Enter mark of C++ :"))

total = a+b+c
percentage = (total/300)*100

if(percentage >= 40 and a>=33 and b>=33 and c>=33):
    print("Congratulation you are pass.")
    print("your percentage is : ", percentage ,"%")
else:
    print("You are failed.")
    print("Your percentage is : " ,percentage ,"%")

