def ascending(a,b,c) :
    if a <= b and a <= c :
        if b <= c :
            return a,b,c 
        else :
            return a,c,b
    elif b <= a and b <= c :
        if a <= c :
            return b,a,c
        else :
            return b,c,a 
    else :
        if a <= b :
            return c,a,b
        else :
            return c,b,a

a = int(input("enter 'A' :"))
b = int(input("enter 'B' :"))
c = int(input("enter 'C' :"))
print ("Ascending order :",ascending(a,b,c))