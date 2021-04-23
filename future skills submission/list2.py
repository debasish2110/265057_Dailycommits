"""
Write a Python program to change the position of every n-th value with the (n+1)th in a lis
"""


def change_pos(my_list):
    for i in range(0, len(my_list), 2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

        return my_list


my_list = [0, 1, 2, 3, 4, 5]

print(change_pos(my_list))

