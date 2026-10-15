# Problem 59: Find LCM of two numbers
a = abs(int(input("Enter first number: ")))
b = abs(int(input("Enter second number: ")))
x, y = a, b
while y:
    x, y = y, x % y          # x is now GCD
lcm = (a * b) // x if x != 0 else 0
print("LCM:", lcm)
