# Problem 89: Sequential number triangle
n = int(input("Enter number of rows: "))
num = 1
for i in range(1, n + 1):
    row = []
    for _ in range(i):
        row.append(str(num))
        num += 1
    print(" ".join(row))
