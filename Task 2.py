# ---------------------------------------------------------
# BITWISE OPERATOR TASKS (1–8)
# ---------------------------------------------------------

print("\nTask 1")
a = 10
b = 6
print(a & b)

print("\nTask 2")
x = 12
y = 5
print(x | y)

print("\nTask 3")
num = 8
print(~num)

print("\nTask 4")
a = 15
b = 9
print(a ^ b)

print("\nTask 5")
num = 7
print(num << 2)

print("\nTask 6")
num = 20
print(num >> 1)

print("\nTask 7")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print("AND =", n1 & n2)

print("\nTask 8")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print("XOR =", n1 ^ n2)

# ---------------------------------------------------------
# STRING TASKS (9–14)
# ---------------------------------------------------------

print("\nTask 9")
print("hi" * 4)

print("\nTask 10")
print("python" * 3)

print("\nTask 11")
print("super" + "man")

print("\nTask 12")
print("hello" + " " + "world")

print("\nTask 13")
name = input("Enter a name: ")
print(name * 5)

print("\nTask 14")
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(s1 + s2)

# ---------------------------------------------------------
# INPUT & TYPE CASTING TASKS (15–20)
# ---------------------------------------------------------

print("\nTask 15")
name = input("Enter your name: ")
print(type(name))

print("\nTask 16")
age = input("Enter age: ")
age = int(age)
print(age)

print("\nTask 17")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)

print("\nTask 18")
m1 = float(input("Enter first mark: "))
m2 = float(input("Enter second mark: "))
print("Average =", (m1 + m2) / 2)

print("\nTask 19")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(3 * a * 2 + b - 2)

print("\nTask 20")
num = input("Enter a number: ")
print("Before casting:", type(num))
num = int(num)
print("After casting:", type(num))

# ---------------------------------------------------------
# UNIT DIGIT TASKS (21–25)
# ---------------------------------------------------------

print("\nTask 21")
num = input("Enter a number: ")
print("Last digit:", num[-1])

print("\nTask 22")
num = int(input("Enter a number: "))
print("Unit digit:", num % 10)

print("\nTask 23")
num = int(input("Enter a number: "))
print("Without last digit:", num // 10)

print("\nTask 24")
num = int(input("Enter a number: "))
print("Second last digit:", (num // 10) % 10)

print("\nTask 25")
num = int(input("Enter a 5-digit number: "))
print("Last digit:", num % 10)

# ---------------------------------------------------------
# IF STATEMENT TASKS (26–30)
# ---------------------------------------------------------

print("\nTask 26")
if 10 >= 5:
    print("10 is greater or equal to 5")

print("\nTask 27")
num = int(input("Enter a number: "))
if num > 50:
    print("Greater than 50")

print("\nTask 28")
age = int(input("Enter age: "))
if age >= 18:
    print("Adult")

print("\nTask 29")
num = int(input("Enter a number: "))
if num > 100:
    print("Greater than 100")

print("\nTask 30")
num = int(input("Enter a number: "))
if num >= 0:
    print("Positive or zero")

# ---------------------------------------------------------
# IF-ELSE TASKS (31–34)
# ---------------------------------------------------------

print("\nTask 31")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

print("\nTask 32")
marks = int(input("Enter marks: "))
if marks >= 35:
    print("Pass")
else:
    print("Fail")

print("\nTask 33")
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
else:
    print("Negative")

print("\nTask 34")
num = int(input("Enter a number: "))
if num > 10:
    print("Greater than 10")
else:
    print("Not greater than 10")

# ---------------------------------------------------------
# NESTED IF TASKS (35–37)
# ---------------------------------------------------------

print("\nTask 35")
age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")

print("\nTask 36")
marks = int(input("Enter marks: "))
age = int(input("Enter age: "))
if marks >= 60:
    if age >= 17:
        print("Admission Granted")
    else:
        print("Admission Denied")
else:
    print("Admission Denied")

print("\nTask 37")
age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))
if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")

# ---------------------------------------------------------
# MATCH STATEMENT TASKS (38–40)
# ---------------------------------------------------------

print("\nTask 38")
n = int(input("Enter a number (1–7): "))
match n:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: print("Invalid")

print("\nTask 39")
n = int(input("Enter (1–3): "))
match n:
    case 1: print("Red")
    case 2: print("Blue")
    case 3: print("Green")
    case _: print("Invalid")

print("\nTask 40")
n = int(input("Enter (1–4): "))
match n:
    case 1: print("Apple")
    case 2: print("Mango")
    case 3: print("Orange")
    case 4: print("Banana")
    case _: print("Invalid")

print("\nAll tasks completed!")
