# Problem 98: Alphabet triangle (row repeat)
n = int(input("Enter number of rows (max 26): "))
for i in range(n):
    letter = chr(ord("A") + i)
    print(" ".join([letter] * (i + 1)))
