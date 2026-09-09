time = int (input ("enter the current hour from 00 to 24 : "))
print (" Greet ")
if time in range (5,12):
    print ("good morning")
elif time in range (12 , 17):
    print ("good afternoon")
elif time in range(17 , 21) :
    print ("good evening")
elif time in range (21 , 25) or time in range(0 , 5):
    print ("good night")
else :
    print ("time is not given in 00 to 24 range")

