# Problem 95: Column-wise incrementing triangle
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print(" ".join(str(k) for k in range(1, i + 1)))
