# Problem 87: Sandglass / Hourglass
n = int(input("Enter half height: "))
# Upper part (inverted pyramid)
for i in range(n):
    print(" " * i + "*" * (2 * (n - i) - 1))
# Lower part (pyramid without the middle row)
for i in range(1, n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
