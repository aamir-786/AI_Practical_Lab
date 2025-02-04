#7.	Write a program to check whether a year is a leap year.
# A year is a leap year if it is divisible by 4. If the year is divisible by 100, then it must be divisible by 400 also.

year = input("Enter a year: ")
if int(year)%4==0 and int(year)%100!=0 or int(year)%400==0:
    print(year," is a leap year.")
else:
    print(year,"is not a leap year.")
    