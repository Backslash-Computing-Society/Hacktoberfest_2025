a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Using third variable
x, y = a, b
temp = x
x = y
y = temp
print(f"Using third variable: a = {x}, b = {y}")

# Without using third variable
a, b = b, a
print(f"Without third variable: a = {a}, b = {b}")