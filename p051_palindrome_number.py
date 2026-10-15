# Problem 51: Check if a number is a palindrome
n = abs(int(input("Enter a number: ")))
temp, rev = n, 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Palindrome" if rev == n else "Not a palindrome")
