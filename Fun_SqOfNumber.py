#Function to make a square of a number

print("===============================================")
print("Find the Square of a number.")
print("===============================================")

num = input("Enter a number to get its square: ")
def square(num):
    return (num*num)

print("Square of the number is: ", square(int(num)) ) #TypeError: can't multiply sequence by non-int of type 'str'