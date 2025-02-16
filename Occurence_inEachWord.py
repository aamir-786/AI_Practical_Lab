# 34.	Write a program to count the number of occurrences of each word in a given string.

print("===============================================")
print("Count the number of occurrences of each word in a given string.")
print("===============================================")

string = input("Enter the String: ")
words = string.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        
print("Occurence of each word in the string is: ", word_count)