# Problem 72: Convert binary to decimal
binary = input("Enter a binary number: ").strip()
value = 0
for bit in binary:
    value = value * 2 + int(bit)
print("Decimal:", value)
