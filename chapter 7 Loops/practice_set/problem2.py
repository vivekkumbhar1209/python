# Write a program to greet all the person names stored in a list ‘l’ and which starts with S. l = ["Harry", "Soham", "Sachin", "Rahul"]

l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if name.startswith("S"):
        print(name)
