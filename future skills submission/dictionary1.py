""""
Write a Python script to merge two Python dictionaries.
"""
def dict_merge(dict1,dict2):
    merge=dict1 | dict2
    return merge

dict1={"Name":"Deba", "Age":22}
dict2={"height":5.8, "weight":"68kg"}
dm= dict_merge(dict1,dict2)   # storing the output of the dict_merge in the variable dm
print(dm)

#this code is contributed by Debashish Dash


