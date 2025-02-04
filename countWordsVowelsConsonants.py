# 24.	Write a program to count the number of words, vowels, and consonants in a string.

print("===============================================")
print("Enter a string to count the number of words, vowels and consonants.")
print("===============================================")

string=input("Enter the string: ")
words=0
vowels=0
consonants=0

for i in string:
    if i in "aeiouAEIOU":
        vowels=vowels+1
    if i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        consonants=consonants+1
    if i==" ":
        words=words+1
print("Number of words in the string are: ",words+1)
print("Number of vowels in the string are: ",vowels)
print("Number of consonants in the string are: ",consonants)

