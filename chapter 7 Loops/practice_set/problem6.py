#  Write a program to print the following star pattern. 
#   * 
#  *** 
# ***** for n = 3

n = 3

for i in range(1, n + 1):
    # Print spaces + stars
    print(" " * (n - i) + "*" * (2 * i - 1))
