# Problem 86: Hollow right-angled triangle
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    if i <= 2 or i == n:
        print("*" * i)
    else:
        print("*" + " " * (i - 2) + "*")
