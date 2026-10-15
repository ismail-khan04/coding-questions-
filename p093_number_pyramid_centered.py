# Problem 93: Number pyramid (centered)
n = int(input("Enter number of rows: "))
for i in range(n):
    row = " ".join(str(k) for k in range(1, 2 * i + 2))
    print(" " * (n - i - 1) + row)
