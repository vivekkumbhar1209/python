name  = 'vivek'

print(len(name))  # print length of string

print(name.endswith('k'))    # check if string ends with 'k'

print(name.startswith('v')) # check if string starts with 'v'

count =  name.count('v')
print(count) # count occurrences of 'v' in string

captilize= name.capitalize()
print(captilize) # capitalize first letter of string

index = name.find('v')
print(index) # find index of substring 've'

replace = name.replace('v','l')
print(replace) # replace 'v' with 'l' in string