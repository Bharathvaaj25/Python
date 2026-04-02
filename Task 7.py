

from abc import ABC, abstractmethod
from functools import reduce


#  TASK 1 & 2: super() + Abstraction

class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


class User(AbstractUser):
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id


class Student(User):
    def __init__(self, name, user_id, dept, fees):
        super().__init__(name, user_id)
        self.dept = dept
        self.fees = int(fees)

    def get_details(self):
        return f"Student | Name: {self.name}, ID: {self.user_id}, Dept: {self.dept}, Fees: {self.fees}"


class Faculty(User):
    def __init__(self, name, user_id, salary):
        super().__init__(name, user_id)
        self.salary = int(salary)

    def get_details(self):
        return f"Faculty | Name: {self.name}, ID: {self.user_id}, Salary: {self.salary}"


class TempFaculty(Faculty):
    def __init__(self, name, user_id, salary, duration):
        super().__init__(name, user_id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty | Name: {self.name}, ID: {self.user_id}, Salary: {self.salary}, Duration: {self.duration} months"


students = []
faculty = []


students.append(Student("Arun Kumar", 1, "CSE", 60000))
students.append(Student("Bala Murugan", 2, "IT", 45000))
students.append(Student("Charan Raj", 3, "ECE", 70000))
students.append(Student("Deepak Sharma", 4, "EEE", 52000))



faculty.append(Faculty("Dr. Kumar", 101, 40000))
faculty.append(Faculty("Prof. Ravi", 102, 28000))
faculty.append(TempFaculty("Suresh Babu", 103, 35000, 6))
faculty.append(TempFaculty("Anita Devi", 104, 32000, 12))


# TASK 3: Sorting

students.sort(key=lambda x: x.fees)
faculty.sort(key=lambda x: x.salary)

print("\n--- SORTED STUDENTS ---")
for s in students:
    print(s.get_details())

print("\n--- SORTED FACULTY ---")
for f in faculty:
    print(f.get_details())


#  TASK 4: map() 

student_names = list(map(lambda s: s.name, students))
print("\nStudent Names:", student_names)


# TASK 5: filter() 

high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

print("\n--- HIGH FEE STUDENTS ---")
for s in high_fee_students:
    print(s.get_details())

print("\n--- HIGH SALARY FACULTY ---")
for f in high_salary_faculty:
    print(f.get_details())


# TASK 6: reduce() 

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("\nTotal Fees:", total_fees)
print("Total Salary:", total_salary)


#  TASK 7: Higher Order Function 

def process_users(users, func):
    return list(map(func, users))

upper_names = process_users(students, lambda s: s.name.upper())
print("\nUppercase Names:", upper_names)



print("\n--- ALL DETAILS ---")

for s in students:
    print(s.get_details())

for f in faculty:
    print(f.get_details())




