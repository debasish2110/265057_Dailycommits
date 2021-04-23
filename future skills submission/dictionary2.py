"""Write a Python program to convert a list into a nested dictionary of keys"""

num_list = [1, 2, 3, 4]
new_dict = current = {}
for ele in num_list:
    current[ele] = {}
    current = current[ele]
print(new_dict)