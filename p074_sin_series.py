# Problem 74: Sum of series x - x^3/3! + x^5/5! - x^7/7! + ... (N terms)
import math

x = float(input("Enter x (in radians): "))
terms = int(input("Enter number of terms: "))
total = 0.0
for i in range(terms):
    power = 2 * i + 1
    term = (x ** power) / math.factorial(power)
    total += term if i % 2 == 0 else -term
print("Sum:", round(total, 6))
