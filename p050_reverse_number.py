# Problem 50: Reverse a number
n = int(input("Enter a number: "))
sign = -1 if n < 0 else 1
reversed_num = sign * int(str(abs(n))[::-1])
print("Reversed number:", reversed_num)
