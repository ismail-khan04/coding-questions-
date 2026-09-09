a = int(input('enter a number : '))
b = int(input('enter a number : '))
c = int(input('enter a number : '))
if a > b and a > c :
    print("a is largest in three numbers")
elif b > c and b > a :
    print ("b is largest in three numbers")
elif c > a and c > b :
    print ('c is largest in three numbers')
elif a == b and a > c :
    print("a is equal to b and greater than c")
else :
    print ("all numbers are equal ")