# Problem 69: Print all factors / divisors of a number
n = abs(int(input("Enter a number: ")))
print("Factors:", end=" ")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
print()
