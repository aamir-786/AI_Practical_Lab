def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

def mod(a, b):
    return a % b if b != 0 else "Cannot find modulus with zero"

def exp(a, b):
    return a ** b

def floor(a, b):
    return a // b if b != 0 else "Cannot perform floor division by zero"

print("===============================================")
print("A simple calculator.")
print("===============================================")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

while True:
    print("\nChoose the operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponent")
    print("7. Floor Division")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Addition is:", add(num1, num2))
    elif choice == '2':
        print("Subtraction is:", sub(num1, num2))
    elif choice == '3':
        print("Multiplication:", mul(num1, num2))
    elif choice == '4':
        print("Division is:", div(num1, num2))
    elif choice == '5':
        print("Mod is:", mod(num1, num2))
    elif choice == '6':
        print("Exponential is :", exp(num1, num2))
    elif choice == '7':
        print("Floor:", floor(num1, num2))
    elif choice == '8':
        print("Exiting calculator. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a valid option.")
