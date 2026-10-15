# Problem 104: Hollow diamond inside a rectangle
n = int(input("Enter n (size of the diamond): "))
width = 2 * n - 1
height = 2 * n - 1
for r in range(height):
    if r == 0 or r == height - 1:
        print(" ".join("*" for _ in range(width)))
        continue
    d = abs(r - (n - 1))
    w = (n - 1) - d
    row = [" "] * width
    row[(n - 1) - w] = "*"
    row[(n - 1) + w] = "*"
    print(" ".join(row))
