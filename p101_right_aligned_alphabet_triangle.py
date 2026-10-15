# Problem 101: Right-aligned alphabet triangle
n = int(input("Enter number of rows (max 26): "))
for i in range(1, n + 1):
    print(" " * (n - i) + " ".join(chr(ord("A") + k) for k in range(i)))
