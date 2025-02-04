# 19.	Write a program to count how many times a specific number appears in a list.

print("===============================================")
print("Enter a list to count how many times a specific number appears in a list.")
print("===============================================")
list = []
for i in range(5):
    list.append(input("Enter the element in the list: "))
num = input("Enter the number to count: ")
count = 0
for i in list:
    if i==num:
        count +=1
        print("Number", num ,"appears", count, "times in the List")