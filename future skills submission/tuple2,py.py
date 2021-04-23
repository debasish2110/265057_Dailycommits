"""
Write a Python program to find the repeated items of a tuple
"""

my_tup = (1, 3, 4, 32, 1, 1, 1, 31, 32, 12, 21, 2, 3)

for i in my_tup:
    if my_tup.count(i) > 1:
        print(i, "->", my_tup.count(i))
