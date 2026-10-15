# Problem 62: Compute 1 - 2 + 3 - 4 + 5 - ... up to N terms
n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    total += i if i % 2 == 1 else -i
print("Sum:", total)
