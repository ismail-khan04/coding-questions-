# Problem 63: Find x^n without using built-in pow()
x = float(input("Enter base x: "))
n = int(input("Enter exponent n: "))
result = 1
for _ in range(abs(n)):
    result *= x
if n < 0:
    result = 1 / result
print("x^n =", result)
