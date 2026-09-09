def valid_triangle (a,b,c) :
    if a+b>c or a+c>b or b+c>a :
        return "Triangle can be formed"
    else :
        return " Can't form a Triangle "

a = int(input("enter side 'A' :"))
b = int(input("enter side 'B' :"))
c = int(input("enter side 'C' :"))

print (valid_triangle(a,b,c))