# Step 1: Create a dictionary of student marks
student_marks = {
    "Alice": 85,
    "David": 92,
}

# Step 2: Ask the user to enter a student name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks or show not found message
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Student '{name}' not found in the record.")
