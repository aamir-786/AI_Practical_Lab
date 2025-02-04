print("===============================================")
print("Prime Numbers between 1 and 50")
print("===============================================")
for num in range(1,51):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
            