a = int(input("enter 'a' :"))
b = int(input("enter 'b' :"))
c = int(input("enter 'c' :"))
D = b*b-4*a*c 
if D > 0 :
    print (" roots are real and distinct ")
    x1 = (-b + (D**0.5))/2*a
    x2 = (-b - (D**0.5))/2*a
    print (x1,x2)
elif D == 0 :
    print (" roots are real and equal ")
    x1 = -b/2*a
else :
    