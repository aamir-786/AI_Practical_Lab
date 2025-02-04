# 23.	Write a program to check if a string is a palindrome.

print("===============================================")
print("Enter a string to check if it is a palindrome.")
print("===============================================")

string=input("Enter the String : ")
revString=""
for i in string:
    revString=i+revString
if string==revString:
        print(string, "is a Palindrome.")
else:
    print(string, "is not a Palindrome.")