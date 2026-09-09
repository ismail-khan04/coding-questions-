def check ( a ):
    if a > 0 :
        match a :
            case _ if a % 2 == 0 :
                return "Number is Positive and Even"
            case _ :
                return "Number is Positive and Odd"
    elif a < 0 :
        return "Number is Negative"
    else :
        return "Number is equal to zero"

a = int(input("enter 'A' :"))
print (check(a))