#14.	Write a program to calculate the factorial of a given number.

print("===============================================")
print("Enter a number to find the factorial.")
print("===============================================")

num = input("Enter a number: ")
fact = 1
for i in range(1, int(num) + 1):
    fact = fact * i
print("Factorial of", num, "is", fact)
