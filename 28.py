def triangle(a,b,c):
    if a==b==c :
        return "Equilateral Triangle"
    elif a!=b!=c :
        return "Scalene Triangle"
    elif a==b!=c or a!=b==c :
        return "Isosceles Triangle"
    else :
        return "Right Triangle"

print ("enter the sides of the triangle :")
a = int(input("enter side 'A' :"))
b = int(input("enter side 'B' :"))
c = int(input("enter side 'C' :"))


print  ( triangle(a,b,c))