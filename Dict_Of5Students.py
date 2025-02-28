# 31.	Write a program to create a dictionary of 5 students with their marks and display it.

print("===============================================")
print("Create a dictionary of 5 students with their marks and display it.")
print("===============================================")

students = {"St1": 90, "St2": 80, "St3": 70, "St4": 60, "St5": 50} 
print("Students with their marks are: ", students)

# 32.	Write a program to update the marks of a specific student in the dictionary.

print("===============================================")
print("Update the marks of a specific student in the dictionary.")
print("===============================================")

students["St3"] = 75
print("Updated Dictionary: ", students)



# 33.	Write a program to find the student with the highest marks.

print("===============================================")
print("Find the student with the highest marks.")
print("===============================================")

maxMarks = max(students.values())
for key, value in students.items():
    if value == maxMarks:
        print("Student with highest marks is: ", key, value)