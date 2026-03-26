
students = {
"Bharathvaaj": ["Math", "Science"],
    "Yogi": ["English", "History"]
}


def add_student(name, course_list):
    students[name] = course_list
    print(f"{name} added successfully!")


def update_courses(name, new_course):
    if name in students:
        students[name].append(new_course)
        print(f"Course '{new_course}' added to {name}")
    else:
        print("Student not found!")


def display_students():
    print("\n--- Student Details ---")
    for name, courses in students.items():
        print(f"{name}: {courses}")



print("Initial Data:")
display_students()

print("\nAdding new student...")
add_student("Harthik", ["Physics", "Chemistry"])

print("\nUpdating courses...")
update_courses("Bharathvaaj", "Computer Science")

print("\nFinal Data:")
display_students()