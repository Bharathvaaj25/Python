def calculate_total(marks):
    """Calculate total marks from list of 3 subject marks"""
    return sum(marks)

def calculate_average(total, num_subjects=3):
    """Calculate average marks"""
    return total / num_subjects

def get_grade(average):
    """Return grade based on average marks"""
    if average >= 90:
        return 'A+'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'

def print_report_card(student_data):
    """Print formatted report card"""
    name = student_data['name']
    marks = student_data['marks']
    subjects = ['Maths', 'Science', 'English']
    
    total = calculate_total(marks)
    average = calculate_average(total)
    grade = get_grade(average)
    
    print("=" * 50)
    print("         STUDENT REPORT CARD")
    print("=" * 50)
    print(f"Student Name: {name.upper()}")
    print("-" * 50)
    
    print(f"{'Subject':<12} {'Marks':<8} {'Grade':<5}")
    print("-" * 35)
    
    for i, (subject, mark) in enumerate(zip(subjects, marks)):
        subj_grade = get_grade(mark)
        print(f"{subject:<12} {mark:<8} {subj_grade:<5}")
    
    print("-" * 35)
    print(f"Total: {'':<12} {total:<8} {'':<5}")
    print(f"Average: {'':<12} {average:<8.1f} {grade:<5}")
    print("=" * 50)
    print()

if __name__ == "__main__":
    # Fixed - call the functions properly
    student1 = {
        'name': 'Ravi Kumar',
        'marks': [85, 92, 78]
    }
    
    student2 = {
        'name': 'bharathvaaj',
        'marks': [72, 68, 81]
    }

    print_report_card(student1)
    print_report_card(student2)
    
    # Interactive mode
    print("Enter new student details:")
    new_name = input("Student Name: ")
    print("Enter marks for 3 subjects (Maths, Science, English):")
    new_marks = []
    for i in range(3):
        mark = float(input(f"Subject {i+1}: "))
        new_marks.append(mark)
    
    new_student = {
        'name': new_name,
        'marks': new_marks
    }
    
    print_report_card(new_student)


