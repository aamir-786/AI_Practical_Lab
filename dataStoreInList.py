# 15.	Write a program to take 5 numbers as input from the user, store them in a list, and display the list.

print("===============================================")
print("Enter 5 numbers to store them in a list.")
print("===============================================")

num=[]
for i in range(5):
    n = input("Enter Number: ")
    num.append(n)
      
print("List of numbers entered by you are: ",num)


#16.	Write a program to calculate the sum and average of elements in a list.
print("===============================================")
print("Print the Sum and Average of Above List.")
print("===============================================")

sum=0
for i in num:
    sum =sum+int(i)
print("Sum of numbers in the list is: ",sum)

avg = sum/len(num)
print("Average of numbers in the list is: ",avg)
  