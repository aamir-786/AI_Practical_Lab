#12.	Write a program to count the number of vowels in a string.

print("===============================================")
print("Enter a string to count the number of vowels.")
print("===============================================")

string=input("Enter the string: ")
vowels=0
for i in string:
    if i in "aeiouAEIOU":
        vowels=vowels+1 
print("Number of vowels in the string are: ",vowels)