# Problem 77: Print numbers in increasing order and then decreasing order (single recursive function)
def pattern(n, i=1):
    print(i, end=" ")
    if i < n:
        pattern(n, i + 1)
    print(i, end=" ")

n = int(input("Enter N: "))
pattern(n)
print()
