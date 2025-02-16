#10.	Write a program to calculate the sum of numbers from 1 to n, where n is entered by the user.
#
num=input("Enter a number: ")
sum=0
for i in range(1,int(num)+1):
    sum=sum+i
print("Sum of numbers from 1 to",num,"is",sum)

#11.	Write a program to calculate the factorial of a given number.
#
print("===============================================")
print("Enter a number to find the factorial.")
print("===============================================")
num=input("Enter a number: ")
fact=1
for i in range(1,int(num)+1):
    fact=fact*i
print("Factorial of",num,"is",fact)
