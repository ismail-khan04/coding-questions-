# Problem 109: X pattern
n = int(input("Enter n (odd size recommended): "))
for i in range(n):
    row = [" "] * n
    row[i] = "*"
    row[n - 1 - i] = "*"
    print(" ".join(row))
