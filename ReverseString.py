# 22.	Write a program to reverse a string without using slicing.

print("===============================================")
print("Enter a string to reverse it.")
print("===============================================")

string= input("Enter the String:")
revString=""
for i in string:
    revString=i+revString 
print("Reversed String is: ", revString)  
