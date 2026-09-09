a = int(input(' enter a number :'))
b = int(input(' enter a number :'))
print( "a and b before swap",a,b)
a = a^b
b = a^b
a = a^b
print( "a and b after swap",a,b)
