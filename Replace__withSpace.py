# 25.	Write a program to replace all spaces in a string with an underscore (_).

print("===============================================")
print("Enter a string to replace all spaces with _")
print("===============================================")

string= input("Enter the String:")
newString=""
for i in string:
    if i==" ":
        newString=newString+"_"
    else:
        newString=newString+i
        
        print("String after replacing spaces with _ is: ", newString)
        break