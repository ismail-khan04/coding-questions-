# Problem 108: Right arrow pattern
n = int(input("Enter n (arrow size): "))
# Arrow head (growing, then shrinking)
for i in range(1, n + 1):
    print("*" * i)
# Shaft
print("*" * (2 * n))
for i in range(n - 1, 0, -1):
    print("*" * i)
