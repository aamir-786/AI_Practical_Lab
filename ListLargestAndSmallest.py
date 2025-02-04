
# 17.	Write a program to find the largest and smallest elements in a list.
num=[23,45,67,89,12,34,56,78,90,11]
print("===============================================")
print("Print the Largest and Smallest Number in the List.")
print("===============================================")

largest=num[0]
smallest=num[0]
for i in num:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
print("Largest Number in the list is: ",largest)
print("Smallest Number in the list is: ",smallest)
