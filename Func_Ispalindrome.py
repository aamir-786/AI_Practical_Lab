# 29.	Write a function to check if a string is a palindrome.

print("===============================================")
print("Check if a string is a palindrome.")
print("===============================================")

string= input("Enter the String:")
def IsPlaindrome(string):
    revString=""
    for i in string:
        revString=i+revString 
    if string==revString:
        return "Palindrome"
    else:
        return "Not Palindrome"
    
print("String is: ", IsPlaindrome(string))