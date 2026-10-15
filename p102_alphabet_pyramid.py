# Problem 102: Alphabet pyramid (centered)
n = int(input("Enter number of rows (max 26): "))
for i in range(n):
    left = [chr(ord("A") + k) for k in range(i + 1)]
    row = left + left[-2::-1]
    print(" " * (n - i - 1) + " ".join(row))
