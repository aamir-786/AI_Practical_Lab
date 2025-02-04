# 20.	Write a program to sort a list in ascending order.

print("===============================================")
print("Enter a list to sort it in ascending order.")
print("===============================================")

list= []
for i in range(5):
    list.append(input("Enter the element in the List:"))
    
    list.sort()
    print("Sorted List in Ascending order is: ", list)