
# Task 1 – Print Formatting

print("Hello", "World", "Welcome", "Python", sep=" ")
print("Laptop", "Mouse", "Keyboard", sep=" | ")

# -----------------------------
# Task 2 – Variables (one-line with '-')
# -----------------------------
name = "Ravi"
age = 22
city = "Chennai"
print(f"{name}-{age}-{city}")

# -----------------------------
# Task 3 – Multiple Assignment
# -----------------------------
name, age, student = "Meena", 20, True
print(name, age, student)

# -----------------------------
# Task 4 – Indexing
# -----------------------------
word = "Python"
print(word[0])   # First letter
print(word[2])   # Third letter
print(word[-1])  # Last letter

# -----------------------------
# Task 5 – Arithmetic Operators
# -----------------------------
print(25 + 10)
print(50 - 20)
print(8 * 5)
print(100 / 10)  # true division -> float
print(10 % 3)
print(2 ** 4)
print(20 // 3)   # floor division

# -----------------------------
# Task 6 – BODMAS / Operator Precedence
# -----------------------------
print(3 + 2 * 5 ** 2)  # 53

# -----------------------------
# Task 7 – Assignment Operator
# -----------------------------
num = 50
num += 25
print(num)

num = 100
num /= 10
print(num)  # 10.0

# -----------------------------
# Task 8 – Comparison Operators
# -----------------------------
print(10 > 5)
print(20 < 15)
print(5 == 5)
print(10 != 8)
print(7 >= 7)
print(6 <= 2)

# -----------------------------
# Task 9 – String Comparison (case-sensitive)
# -----------------------------
a = "apple"
b = "Apple"
print(a == b)  # False

# -----------------------------
# Task 10 – Logical Operators
# -----------------------------
print(10 > 5 and 5 == 5)
print(5 > 10 or 10 == 10)
print(not (5 > 2))

# -----------------------------
# Task 11 – Membership Operators
# -----------------------------
numbers = [10, 20, 30, 40, 50]
print(20 in numbers)
print(60 in numbers)
print(30 not in numbers)

# -----------------------------
# Task 12 – Swap Variables (single-line)
# -----------------------------
a = 10
b = 20
a, b = b, a
print("a =", a)
print("b =", b)

# -----------------------------
# Task 13 – Bitwise XOR
# -----------------------------
a = 6
b = 3
print(a ^ b)  # 5
