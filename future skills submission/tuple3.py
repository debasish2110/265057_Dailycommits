"""
Write a Python program to convert a list of tuples into a dictionary
"""


def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di


tups = [("Debashish", 22), ("shivam", 21), ("Aayush", 21),
        ("Himanshu", 20), ("Pushpak", 25), ("Aman", 23),
        ("Saurabh", 21), ("Subham", 50)]
dictionary = {}
print(Convert(tups, dictionary))
