my_list = ["A", "B", "C","D","E"]
print(my_list)

my_mix_list = [1,2.0,True,"LTTS",(0,1,2)]
print(my_mix_list)

# Accessing list elements
print(my_list[2])
print(my_list)
print(my_mix_list)
print(my_mix_list[4][0])
print(my_mix_list[-1])

#ranging
print(my_list[2:])
print(my_list[:4])
print(my_list[::-1]) #reversing a list
print(my_list[::2]) #every 2nd element of the list
print(my_list[-3:1:-1])

my_list[0]="Z"
print(my_list)

my_list.insert(2,"X")
print(my_list)

my_list.append("F")
print(my_list)

my_list.extend(my_mix_list)
print(my_list)

my_list.remove('B')
print(my_list)

print(my_list.pop())
print(my_list)

for item in my_list:
    print(item)

[print(x) for x in my_list]

"""comp=[x for x in my_list if "A" in x]
print(comp)"""

l1=[4,3,1,6,5,8,3]
l1.sort()
print(l1)

l1.sort(reverse=True)
print(l1)

#solution submitted by Debashish
