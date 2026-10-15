# Problem 85: Hollow rectangle
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
for r in range(rows):
    if r == 0 or r == rows - 1:
        row = ["*"] * cols
    else:
        row = ["*" if c in (0, cols - 1) else " " for c in range(cols)]
    print(" ".join(row))
