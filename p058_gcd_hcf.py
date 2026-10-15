# Problem 58: Find GCD / HCF of two numbers (Euclidean algorithm)
a = abs(int(input("Enter first number: ")))
b = abs(int(input("Enter second number: ")))
x, y = a, b
while y:
    x, y = y, x % y
print("GCD / HCF:", x)
