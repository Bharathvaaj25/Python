
employees = [
    {"name": "Ravi", "age": 25, "role": "Developer", "salary": 30000},
    {"name": "Priya", "age": 28, "role": "Designer", "salary": 28000},
    {"name": "Arun", "age": 30, "role": "Manager", "salary": 40000},
    {"name": "Karthik", "age": 26, "role": "Tester", "salary": 25000},
    {"name": "Meena", "age": 27, "role": "HR", "salary": 27000},
    {"name": "Suresh", "age": 32, "role": "Team Lead", "salary": 45000},
    {"name": "Anitha", "age": 24, "role": "Support Engineer", "salary": 22000},
    {"name": "Vikram", "age": 29, "role": "Analyst", "salary": 31000}
]

while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Show Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Employee
    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        role = input("Enter role: ")
        salary = float(input("Enter salary: "))

        emp = {
            "name": name,
            "age": age,
            "role": role,
            "salary": salary
        }

        employees.append(emp)
        print("Employee added!")

    # Show Employees
    elif choice == "2":
        if len(employees) == 0:
            print("No employees found")
        else:
            print("\nEmployee List:")
            for i in range(len(employees)):
                e = employees[i]
                print(i + 1, e["name"], e["age"], e["role"], e["salary"])

    # Update Employee
    elif choice == "3":
        if len(employees) == 0:
            print("No employees to update")
        else:
            for i in range(len(employees)):
                print(i + 1, employees[i]["name"])

            num = int(input("Enter employee number: ")) - 1

            if num >= 0 and num < len(employees):
                name = input("Enter new name: ")
                age = input("Enter new age: ")
                role = input("Enter new role: ")
                salary = input("Enter new salary: ")

                if name != "":
                    employees[num]["name"] = name
                if age != "":
                    employees[num]["age"] = int(age)
                if role != "":
                    employees[num]["role"] = role
                if salary != "":
                    employees[num]["salary"] = float(salary)

                print("Employee updated!")
            else:
                print("Invalid number")

    # Delete Employee
    elif choice == "4":
        if len(employees) == 0:
            print("No employees to delete")
        else:
            for i in range(len(employees)):
                print(i + 1, employees[i]["name"])

            num = int(input("Enter employee number: ")) - 1

            if num >= 0 and num < len(employees):
                employees.pop(num)
                print("Employee deleted!")
            else:
                print("Invalid number")

    # Exit
    elif choice == "5":
        print("Program ended")
        break

    else:
        print("Wrong choice")
