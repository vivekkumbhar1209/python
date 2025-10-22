# Write a program to find out whether a given post is talking about “Harry” or not.

# post = "Hey Harry bhai is good Harry is very good abd harry is great"

post = input("enter the post")

if("Harry".lower() in post.lower()):
    print("This post talking about harry")
else:
    print("this post not talking about harry")
