# Problem 105: Number diamond
n = int(input("Enter number of rows (half height): "))
for i in range(1, n + 1):
    nums = list(range(1, i + 1)) + list(range(i - 1, 0, -1))
    print(" " * (n - i) + " ".join(str(x) for x in nums))
for i in range(n - 1, 0, -1):
    nums = list(range(1, i + 1)) + list(range(i - 1, 0, -1))
    print(" " * (n - i) + " ".join(str(x) for x in nums))
