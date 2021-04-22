"""
Write Python code that asks a user how many pizza slices they want.The pizzeria charges Rs 123.00 a slice.
if user order even number of slices, price per slice is Rs 120.00.
Print the total price depending on how many slices user orders.

"""

hmp=int(input("How many pizza slices?? : "))
total=0
if hmp % 2 == 0:
    total= hmp*120.00
else:
    total= hmp*123.00
print(total)


