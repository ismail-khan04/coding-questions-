# Problem 70: Check if a number is a perfect number (sum of proper divisors == number)
n = int(input("Enter a number: "))
total = 0
for i in range(1, n):
    if n % i == 0:
        total += i
print("Perfect number" if n > 0 and total == n else "Not a perfect number")
