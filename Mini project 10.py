



num = 1234567

def convert_number(n):
    print("Binary      :", bin(n))
    print("Octal       :", oct(n))
    print("Hexadecimal :", hex(n))


def format_number(n):
    print("\nFormatted with commas :", format(n, ","))
    print("Scientific notation   :", format(n, ".2e"))



print("Original Number:", num)

print("\n--- Conversions ---")
convert_number(num)

print("\n--- Formatting ---")
format_number(num)