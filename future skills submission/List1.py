"""
Write a Python program to find the second smallest number in a list
"""


def find_sec_smallest(list):
    list.sort()
    print("The sorted list: ", list)
    return list[1]

my_list = []
n = int(input("Enter the number of elements: "))
for i in range(1, n + 1):
    elem = int(input("Enter the elements: "))
    my_list.append(elem)
print("list elements: ", my_list)

print("The second smallest value of this list: ", find_sec_smallest(my_list))
