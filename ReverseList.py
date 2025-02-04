# 18.	Write a program to reverse a list.

print("===============================================")
print("Enter a list to reverse it.")
print("===============================================")
list1 = []
for i in range(5):
    list1.append(input("Enter the element: "))
list1.reverse()
print("Reversed list is: ", list1)
