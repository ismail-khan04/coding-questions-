# Problem 83: Inverted pyramid
n = int(input("Enter number of rows: "))
for i in range(n):
    print(" " * i + "*" * (2 * (n - i) - 1))
