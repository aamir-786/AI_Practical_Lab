#11.	Write a program to display the multiplication table of a number entered by the user.

print("===============================================")
print("Enter a number to display the multiplication table.")
print("===============================================")

num=input("Enter the Number:") 
for i in range(1,11):
    print(num,"*",i, "=",int(num)*i)
    