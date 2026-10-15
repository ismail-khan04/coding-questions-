# Problem 110: Plus (+) pattern
n = int(input("Enter n (odd size recommended): "))
mid = n // 2
for i in range(n):
    row = [" "] * n
    if i == mid:
        row = ["*"] * n
    else:
        row[mid] = "*"
    print(" ".join(row))
