# Problem 55: Find factorial of N
n = int(input("Enter N: "))
fact = 1
for i in range(2, n + 1):
    fact *= i
print("Factorial:", fact)
