#8.	Write a program to classify a person's age:
#o	Age < 13 → Child
#o	13 <= Age < 20 → Teenager
#o	Age >= 20 → Adult

age=input("Enter your age: ")
if int(age)<13:
    print("Child")
elif int(age)>=13 and int(age)<20:
    print("Teenager")
else:
    print("Adult")
    