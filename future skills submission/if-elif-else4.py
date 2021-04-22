"""
Write a python program to check if the input number
is-real number
float numner
string
complex number
Zero(0)
"""

number= 1+7j

if type(number) == type(1):
    print("Entered number is a Real Number...")
elif type(number) == type(1.0):
    print("Entered number is a Float Number...")
elif type(number) == type("Abc"):
    print("Entered number is a String...")
elif type(number) == type(1 + 2j):
    print("Entered number is a complex number...")
elif number == 0:
    print("Entered number is 0...")
else:
    print("unknown type...")