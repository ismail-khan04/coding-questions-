# Problem 88: Number triangle (row-wise): row i prints i, i times
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print(" ".join([str(i)] * i))
