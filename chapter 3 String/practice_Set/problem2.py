# Write a program to fill in a letter template given below with name and date. 
# letter = '''  
# Dear <|Name|>, 
# You are selected! 
# <|Date|> 
# '''


letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
# '''
# name = input("Enter your name: ")
# date = input("Enter date: ")
letter = letter.replace("<|Name|>", "vivek")
letter = letter.replace("<|Date|>", "27 oct 2025")
print(letter)

