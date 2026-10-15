# Problem 111: Heart shape pattern (drawn using the heart equation)
for y in range(12, -13, -1):
    line = ""
    for x in range(-30, 31):
        X, Y = x / 15.0, y / 6.0
        if (X ** 2 + Y ** 2 - 1) ** 3 - (X ** 2) * (Y ** 3) <= 0:
            line += "*"
        else:
            line += " "
    print(line.rstrip())
