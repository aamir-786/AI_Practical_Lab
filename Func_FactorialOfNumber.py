# 28.	Write a function to calculate the factorial of a number.

print("===============================================")
print("Calculate the factorial of a number.")
print("===============================================")

num = input("Enter a number to Calculate its Factorial: ")


def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact
   
    print("Factorial of the number is: ", factorial(int(num)))
    