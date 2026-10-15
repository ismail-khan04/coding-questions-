# Problem 52: Happy Number
# Replace the number with the sum of squares of its digits until it reaches 1 (happy)
# or enters a cycle (not happy).
n = abs(int(input("Enter a number: ")))
seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    n = sum(int(d) ** 2 for d in str(n))
print("Happy number" if n == 1 else "Not a happy number")
