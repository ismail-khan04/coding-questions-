# Problem 103: Butterfly pattern
n = int(input("Enter half height: "))
# Upper half
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i) * 2) + "*" * i)
# Lower half
for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i) * 2) + "*" * i)
