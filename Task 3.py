

# 1. Print numbers 1 to 50
for i in range(1, 51):
    print(i)

# 2. Print even numbers 1 to 100
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

# 3. Print odd numbers 1 to 100
for i in range(1, 101):
    if i % 2 != 0:
        print(i)

# 4. Multiplication table of 7
for i in range(1, 11):
    print(7, "x", i, "=", 7*i)

# 5. Sum of numbers 1 to 100
total = 0
for i in range(1, 101):
    total += i
print("Sum =", total)

# 6. Print numbers reverse 50 to 1
for i in range(50, 0, -1):
    print(i)

# 7. Count numbers divisible by 3 (1–100)
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print("Divisible by 3 =", count)

# 8. Squares 1 to 10
for i in range(1, 11):
    print(i*i)

# 9. Cubes 1 to 10
for i in range(1, 11):
    print(i*i*i)

# 10. Print 1 to n
n = int(input("Enter n: "))
for i in range(1, n+1):
    print(i)

# ------------------------------
# SECTION 2 – While Loop (11–15)
# ------------------------------

# 11. Print numbers 1 to 20 using while
i = 1
while i <= 20:
    print(i)
    i += 1

# 12. Factorial using while
n = int(input("Enter number for factorial: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial =", fact)

# 13. Reverse a number using while
n = int(input("Enter number to reverse: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev*10 + digit
    n //= 10
print("Reversed =", rev)

# 14. Count digits in a number
n = int(input("Enter number to count digits: "))
count = 0
if n == 0:
    count = 1
while n > 0:
    count += 1
    n //= 10
print("Digits =", count)

# 15. Keep taking input until "stop"
while True:
    x = input("Enter anything (type 'stop' to end): ")
    if x.lower() == "stop":
        break
    print("You entered:", x)

# --------------------------------
# SECTION 3 – Nested Loops (16–20)
# --------------------------------

# 16. Pattern *
for i in range(1, 5):
    print("*" * i)

# 17. Pattern numbers
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end="")
    print()

# 18. Multiplication table 1 to 5
for n in range(1, 6):
    print("Table of", n)
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)
    print()

# 19. A B C pattern
for i in range(3):
    print("A B C")

# 20. 1 2 3 / 4 5 6 / 7 8 9
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()

# --------------------------------
# SECTION 4 – String Basics (21–25)
# --------------------------------

s = input("Enter string for section 4: ")

# 21. Count characters
print("Characters =", len(s))

# 22. Count vowels
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Vowels =", count)

# 23. Count consonants
count2 = 0
for ch in s:
    if ch.isalpha() and ch not in vowels:
        count2 += 1
print("Consonants =", count2)

# 24. Reverse using loop
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed =", rev)

# 25. Check palindrome
if s.lower() == s[::-1].lower():
    print("Palindrome")
else:
    print("Not palindrome")

# -------------------------------
# SECTION 5 – String Slicing (26–30)
# -------------------------------

s = input("Enter string for section 5: ")

# 26
print(s[:5])

# 27
print(s[-3:])

# 28
print(s[::-1])

# 29
print(s[::2])

# 30
print(s[1:-1])

# ----------------------------
# SECTION 6 – List Basics (31–35)
# ----------------------------

nums = [10, 20, 30, 40, 50]

# 31. Sum
total = 0
for x in nums:
    total += x
print("Sum =", total)

# 32. Max
mx = nums[0]
for x in nums:
    if x > mx:
        mx = x
print("Max =", mx)

# 33. Min
mn = nums[0]
for x in nums:
    if x < mn:
        mn = x
print("Min =", mn)

# 34. Count
count = 0
for _ in nums:
    count += 1
print("Count =", count)

# 35. Check element exists
n = int(input("Enter number to find in list: "))
found = False
for x in nums:
    if x == n:
        found = True
        break
print("Exists?", found)

# ---------------------------------
# SECTION 7 – List Operations (36–40)
# ---------------------------------

nums = [5, 2, 9]

# 36. append 3 values
nums.append(10)
nums.append(20)
nums.append(30)
print(nums)

# 37. Insert at index
nums.insert(1, 100)
print(nums)

# 38. Remove value
nums.remove(20)
print(nums)

# 39. Reverse manually
rev = []
for i in range(len(nums)-1, -1, -1):
    rev.append(nums[i])
print("Reversed:", rev)

# 40. Sort without sort()
sorted_list = []
for x in nums:
    sorted_list.append(x)

for i in range(len(sorted_list)):
    for j in range(i+1, len(sorted_list)):
        if sorted_list[j] < sorted_list[i]:
            sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]

print("Sorted:", sorted_list)
