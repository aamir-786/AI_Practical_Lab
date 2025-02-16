#30.	Write a function to find the maximum of three numbers.

print("===============================================")
print("Find the maximum of three numbers.")
print("===============================================")

def MaxOfThreeNum(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3

num1 = 12;
num2 = 15;
num3 = 10;

print("Maximum of three numbers is: ", MaxOfThreeNum(num1,num2,num3))


