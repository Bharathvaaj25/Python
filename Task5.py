# Task 1: User Info Manager

def create_user(name, age, role):
    return {
        "name": name.title(),
        "age": age,
        "role": role
    }

users = []
users.append(create_user("arun", 21, "developer"))
users.append(create_user("bala", 22, "tester"))
users.append(create_user("charan", 20, "designer"))

print("All Users:")
for user in users:
    print(user)


# Task 2: Dynamic Calculator

def calculate_total(*numbers):
    total = sum(numbers)
    avg = total / len(numbers) if numbers else 0
    return total, avg

print("\nCalculator:")
total, avg = calculate_total(10, 20, 30, 40)
print("Total:", total)
print("Average:", avg)


# Task 3: Keyword Config System

def system_config(**settings):
    print("\nSystem Config:")
    for key, value in settings.items():
        print(f"{key}: {value}")

system_config(mode="debug", version="1.0")


# Task 4: Factorial Service

def factorial(n):
    if n < 0:
        return "Error: Negative number"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("\nFactorial:")
print("Factorial of 5:", factorial(5))
print("Factorial of -3:", factorial(-3))


# Task 5: Memory Optimization (Generator)

def square_generator(n):
    for i in range(n):
        yield i * i

print("\nGenerator vs List:")
gen = square_generator(5)
lst = [i * i for i in range(5)]

print("Generator type:", type(gen))
print("List type:", type(lst))

print("Generator values:")
for val in gen:
    print(val)


# Task 6: Exception Handling

print("\nException Handling:")

try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    result = num / den
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input")

finally:
    print("Program Completed")


# Task 7: File Handling

print("\nFile Handling:")

file = open("team_data.txt", "w")

for user in users:
    file.write(str(user) + "\n")

file.close()

# Read file
file = open("team_data.txt", "r")
content = file.read()
print("File Content:\n", content)

# Check if file is closed
file.close()
print("File closed:", file.closed)
