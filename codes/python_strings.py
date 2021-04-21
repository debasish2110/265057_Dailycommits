
string1="Welcome to LTTS"
print("the input string1 is:",string1)

string2="""this 
way 
we 
can 
write a multiline string"""
print(string2)

#Accessing character in the string
print("first character in the string1 is: ", string1[0])
print("last character of the string1 is: ", string1[-1])

#string slicing
print("3rd to 9th of string1: ", string1[2:10])
print("3rd and 2nd last char: ", string1[2:-2])
print("reversing the string using slicing: ", string1[::-1])
"""string1[2]='E'
print("upading the 2nd char the new string is: (we cannot update a character in the string it will throw an error) ", string1)
"""
string1="I AM LTTS NEXT GEN"
print("after upating the whole string: ", string1)

"""same way we can not delete a character from a string but we can delete an entire string"""


