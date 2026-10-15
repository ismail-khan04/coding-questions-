# Problem 92: Pascal's triangle
n = int(input("Enter number of rows: "))
for i in range(n):
    value = 1
    row = []
    for j in range(i + 1):
        row.append(str(value))
        value = value * (i - j) // (j + 1)
    print(" " * (n - i - 1) + " ".join(row))
