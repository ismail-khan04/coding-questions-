# Problem 99: Alphabet triangle (sequential)
n = int(input("Enter number of rows (max 26): "))
for i in range(1, n + 1):
    print(" ".join(chr(ord("A") + k) for k in range(i)))
