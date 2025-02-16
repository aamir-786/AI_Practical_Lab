#27.	Write a function to check if a number is even or odd.
print("===============================================")
print("Check if a number is even or odd.")
print("===============================================")


num = input("Enter a number to check if it is even or odd: ")
def evenOdd(num):
    if int(num)%2==0:
        return "Even"
    else:
        return "Odd"
print("Number is: ", evenOdd(int(num)))