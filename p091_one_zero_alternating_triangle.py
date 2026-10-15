# Problem 91: 1-0 alternating triangle
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print(" ".join("1" if j % 2 == 0 else "0" for j in range(i)))
