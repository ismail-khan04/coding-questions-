# Problem 71: Convert decimal to binary
n = int(input("Enter a decimal number: "))
if n == 0:
    print("Binary: 0")
else:
    sign = "-" if n < 0 else ""
    n = abs(n)
    bits = ""
    while n > 0:
        bits = str(n % 2) + bits
        n //= 2
    print("Binary:", sign + bits)
