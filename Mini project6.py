


name = "Bharath"
product = "Laptop"

# Formatted sentence
sentence = f"{name} purchased a {product}."

print("Formatted Sentence:")
print(sentence)

# Padding examples
print("\n--- Padded Output ---")

print("Left Align  : ", sentence.ljust(40, "-"))
print("Right Align : ", sentence.rjust(40, "-"))
print("Center Align: ", sentence.center(40, "-"))

