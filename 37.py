def quadrant(x,y) :
    if (x==y==0) :
        return "Point is on origin "
    elif (x > 0 and y > 0) :
        return "Point is in 1st quadrant"
    elif (x < 0 and y > 0) :
        return "Point is in 2nd quadrant "
    elif (x < 0 and y < 0) :
        return "Point is in 3rd quadrant "
    else :
        return "Point is in 4th quadrant"

x = int (input("enter x coordinate : "))
y = int (input("enter y coordinate : "))
print (quadrant(x,y))