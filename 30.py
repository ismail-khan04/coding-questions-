def calculator(a,b,op) :
    match op :
        case '+' :
            return a+b 
        case '-' :
            return a-b 
        case '*' :
            return a*b 
        case '/' :
            return a/b 
        case _ :
            return 'invalid operator'

a = int(input("enter 'A' :"))
b = int(input("enter 'B' :"))
op = input("enter the operator (+,-,*,/) :")
print (calculator(a,b,op))